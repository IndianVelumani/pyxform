'''
Export 'Survey' objects to CSV-or-XLS-formatted XLSForms. Aliased and available 
as methods on 'Survey' objects.

.. module:: survey_to_xlsform
    :Date: 2014/09/24

.. codeauthor: Esmail Fadae <esmail.fadae@kobotoolbox.org>
'''


import base64
import re
import os
import cStringIO
from tempfile import NamedTemporaryFile

import pandas

import pyxform.question
import pyxform.aliases
from pyxform import constants
from pyxform.errors import PyXFormError


class XlsFormExporter():
    
    CASCADING_SELECT_WARNING= u'Cascading-select (choice filter) questions not currently supported. Question choices for any such questions have not been imported.'
    CASCADING_SELECT_SAD_CHOICE_NAME= u'question_choices_not_imported'
    CASCADING_SELECT_SAD_CHOICE_LABEL= u'Apologies, your choices for this (cascading-select) question could not be automatically imported.'
    
    def __init__(self, survey, warnings=None):
        '''
        Prepare a representation of the survey ready to be easily exported as a 
        XLSForm spreadsheet.

        :param pyxform.survey.Survey survey: The survey to be exported.
        :param list warnings: Optional list into which any warnings generated during export will be appended.
        '''
        
        # TODO: Repeats, 'or_other', hints, constraints, ...
        
        self.survey_sheet_df= pandas.DataFrame()
        self.choices_sheet_df= pandas.DataFrame()
        self.settings_sheet_df= pandas.DataFrame()

        # Keep track of 'label' columns.
        self.survey_label_columns= set()
        self.choices_label_columns= set()
        
        # Keep track of any warnings generated.
        if warnings is not None:    # Could be an empty list.
            self.warnings= warnings
        else:
            self.warnings= list()
        
        self.record_settings(survey)
        
        for survey_child in survey['children']:
            if isinstance(survey_child, pyxform.question.Question):
                self.record_question_data(survey_child)
            elif isinstance(survey_child, pyxform.section.GroupedSection):
                self.record_grouped_section(survey_child)
            else:
                raise PyXFormError('Unexpected survey child type "{}".'.format(type(survey_child)))
        
        self.sheet_dfs= {
          constants.SURVEY:     self.survey_sheet_df,
          constants.CHOICES:    self.choices_sheet_df,
          constants.SETTINGS:   self.settings_sheet_df,
        }


    def record_question_data(self, question):
        '''
        Record the given question and any associated data such as the options 
        for multiple-choice questions.
        
        :param pyxform.question.Question question:
        '''
        
        # Buffer the question's eventual additions to the 'survey' sheet.
        survey_row= dict()
        
        question_name= question[constants.NAME]
        xlsform_question_type= pyxform.aliases.get_xlsform_question_type(question[constants.TYPE])
        
        if isinstance(question, pyxform.question.MultipleChoiceQuestion):
            # Special handling for select-type questions.
            
            # Check that the reported 'type' matches the object type.
            if xlsform_question_type not in \
              [constants.SELECT_ONE_XLSFORM, constants.SELECT_ALL_THAT_APPLY_XLSFORM]:
                raise PyXFormError('Unexpected multiple-choice question type "{}"'.format(question['type']))
            
            
            # TODO: Would be nice to reuse the 'list name' when encountering reused sets of choices.
            # Generate a 'list name' comprised of the question name followed by 8 random bytes cast to string.
            list_name= question_name + '_' + base64.urlsafe_b64encode(os.urandom(8))
            
            # Strip out any non-alphanumeric characters so KoBoForm can import. \
            #   Decreasing the space of possible strings, while an egregious \
            #   affront, should be safe.
            list_name= re.compile('[\W_]+').sub('_', list_name)
            
            survey_row[constants.TYPE]= xlsform_question_type + ' ' + list_name
            
            # TODO: Handle cascading-select questions (http://opendatakit.github.io/odk-xform-spec/#secondary-instances).
            # If the question appears to be a cascading-select, report in the \
            #   output that the question choices could not be gathered.
            if question.is_cascading_select():
                manual_sad_choice_row= \
                  {constants.LIST_NAME: list_name,
                   constants.NAME: self.CASCADING_SELECT_SAD_CHOICE_NAME,
                   constants.LABEL: self.CASCADING_SELECT_SAD_CHOICE_LABEL
                   }
                self.choices_sheet_df= pandas.concat([self.choices_sheet_df, pandas.DataFrame.from_dict([manual_sad_choice_row])])
                if self.CASCADING_SELECT_WARNING not in self.warnings:
                    self.warnings.append(self.CASCADING_SELECT_WARNING)
                
            else:
                # Extract and record the choices.
                for question_choice in question[constants.CHILDREN]:
                    self.record_question_choice(question_choice, list_name)
            
        # Non-select questions
        else:
            survey_row[constants.TYPE]= xlsform_question_type

        # Mandatory column 'name'.
        survey_row[constants.NAME]= question_name
        
        # Mandatory 'label' column(s).
        question_labels= self.get_survey_element_label(question)
        survey_row.update(question_labels)
        self.survey_label_columns.update(question_labels.keys()) # Track any new label columns encountered.

        if xlsform_question_type == constants.CALCULATE_XLSFORM:
            survey_row['calculation']= question[constants.BIND][constants.CALCULATE_XLSFORM]

        # Add the row into the 'survey' sheet.
        self.survey_sheet_df= pandas.concat([self.survey_sheet_df, pandas.DataFrame.from_dict([survey_row])])


    def record_question_choice(self, question_choice, list_name):
        '''
        Record the information for an individual choice from a multiple-choice question.
        
        :param pyxform.question.Option question_choice: The choice being imported.
        :param str list_name: A unique identifier for the set of choices this choice belongs to.
        '''
        
        # Mandatory column 'list name'.
        choices_row= {constants.LIST_NAME: list_name}
        # Mandatory column 'name'.
        choices_row[constants.NAME]= question_choice[constants.NAME]
        # Mandatory 'label' column(s).
        choice_labels= self.get_survey_element_label(question_choice)
        choices_row.update(choice_labels)
        
        # Track any new label columns (translations like 'label::English') encountered.
        self.choices_label_columns.update(choice_labels.keys())
        
        # Add the row into the 'choices' sheet.
        self.choices_sheet_df= pandas.concat([self.choices_sheet_df, pandas.DataFrame.from_dict([choices_row])])
        

    def record_grouped_section(self, grouped_section):
        '''
        Record the data associated with a group of questions.
        
        :param pyxform.section.GroupedSection grouped_section:
        '''
        
        # Record the question group and return.
        
        if grouped_section[constants.NAME] == constants.META_XFORM:
            # Do not export the 'meta' group as it is automatically added by 'pyxform'.
            return
        
        # Generate and insert the group's header.
        group_header= {constants.TYPE: u'begin group'}
        if constants.NAME in grouped_section:
            group_header[constants.NAME]= grouped_section[constants.NAME]
        if constants.LABEL in grouped_section:
            question_labels= self.get_survey_element_label(grouped_section)
            group_header.update(question_labels)
        self.survey_sheet_df= pandas.concat([self.survey_sheet_df, pandas.DataFrame.from_dict([group_header])])
        
        # Insert the grouped questions.
        for question in grouped_section['children']:
            self.record_question_data(question)
        
        # Insert the group's footer.
        group_footer= {constants.TYPE: u'end group'}
        self.survey_sheet_df= pandas.concat([self.survey_sheet_df, pandas.DataFrame.from_dict([group_footer])])


    def record_settings(self, survey):
        '''
        Record the information for the 'settings' sheet, if present.
        
        :param pyxform.survey.Survey:
        '''

        # TODO: More potential settings listed at xlsform.org.
        if constants.NAME in survey:
            self.settings_sheet_df['form_id']= [survey[constants.NAME]]
        if constants.TITLE in survey:
            self.settings_sheet_df['form_title']= [survey[constants.TITLE]]


    @staticmethod
    def get_survey_element_label(survey_element):
        '''
        Return a dictionary containing the survey element's singular label or its 
        translations, if present, ready for export to an XLSForm. Labels are keyed 
        by 'label' or 'label::Language'.

        :param pyxform.survey.SurveyElement survey_element:
        :type survey_element: pyxform.question.Question or pyxform.question.Option
        :return: Spreadsheet data (in rows) keyed by sheet name.
        :rtype: {str: DataFrame}
        '''
        
        labels= dict()
        if isinstance(survey_element.get(constants.LABEL), basestring) \
          and (survey_element[constants.LABEL] != ''):
            # Simple label.
            label_column= constants.LABEL
            labels[label_column]= survey_element[constants.LABEL]
        elif survey_element.get(constants.LABEL):
            # Label(s) provided in a 'dict' of translations.
            for language in survey_element[constants.LABEL].iterkeys():
                label_column= constants.LABEL + '::' + language
                labels[label_column]= survey_element[constants.LABEL][language]
        
        return labels


def to_xls(survey, path=None, warnings=None):
    '''
    Convert the provided survey to a XLS-encoded XForm.
    
    :param pyxform.survey.Survey survey:
    :param str path: Optional filesystem path to the desired output file.
    :param list warnings: Optional list into which any warnings generated during export will be appended.
    :returns: If the 'path' parameter was omitted, nothing. Otherwise, a buffer containing the exported form.
    :rtype: NoneType or 'cStringIO.StringIO'
    '''
    
    # Organize the data for spreadsheet output.
    sheet_dfs= XlsFormExporter(survey, warnings).sheet_dfs
    
    # 'pandas.ExcelWriter' operates on file paths, so if the 'path' parameter was omitted, create a temp. file.
    temp_file= None
    if not path:
        temp_file= NamedTemporaryFile(suffix='-pyxform.xls')
        path= temp_file.name
    
    # Write out the data sheet-by-sheet.
    xls_writer= pandas.ExcelWriter(path, encoding='UTF-8')
    for sheet_name, df in sheet_dfs.iteritems():
        df.to_excel(xls_writer, sheet_name, index=False)
    xls_writer.save()
    
    # If a file wasn't desired, return a file-like object with the exported contents.
    if temp_file:
        return cStringIO.StringIO(temp_file.file.read())


def to_csv(survey, path=None, warnings=None):
    '''
    Convert the provided survey to a CSV-formatted XForm.
    
    :param pyxform.survey.Survey survey:
    :param str path: Optional filesystem path to the desired output file.
    :param list warnings: Optional list into which any warnings generated during export will be appended.
    :returns: If the 'path' parameter was omitted, nothing. Otherwise, a buffer containing the exported form.
    :rtype: NoneType or 'cStringIO.StringIO'
    '''
    
    # Organize the data for spreadsheet output.
    sheet_dfs= XlsFormExporter(survey, warnings).sheet_dfs
    
    # Reorganize the data into multi-"sheet" CSV form and export.
    if path:
        csv_buffer= open(path, 'w')
    else:
        csv_buffer= cStringIO.StringIO()
    for sheet_name, df in sheet_dfs.iteritems():
        # Prepend a row of the column names into the sheet.
        csv_df= pandas.concat([pandas.DataFrame(df.columns.to_series()).T, df])
        # Insert column for the sheet name into the sheet and put the name in the first row.
        csv_df= pandas.concat([pandas.DataFrame.from_dict([{'sheet': sheet_name}]), csv_df])
        # Move the 'sheet' column to the front.
        csv_df= csv_df[['sheet']+csv_df.columns.drop('sheet').tolist()]
        
        csv_buffer.write(csv_df.to_csv(header=False, index=False, encoding='UTF-8'))
    csv_buffer.seek(0)
    
    if path:
        csv_buffer.close()
    else:
        return csv_buffer