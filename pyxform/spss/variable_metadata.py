'''
Created on Jun 13, 2014

.. moduleauthor:: Esmail Fadae <efadae@hotmail.com>
'''


from __future__ import unicode_literals
from collections import namedtuple
import json
import re

from .utilities import get_spss_variable_name
from .utilities import get_spss_variable_label
from .utilities import get_spss_value_label

INDENT_STRING= '    '
VALUE_LABELS = 'VALUE_LABELS'
VARIABLE_LABELS = 'VARIABLE_LABELS'

class ValueLabel:

    def __init__(self, value_name, value_label):
        self._name= value_name
        self._label= value_label

    @property
    def name(self):
        '''Read-only accessor to the value's name or encoding.'''
        return self._name

    @property
    def label(self):
        '''Read-only accessor to the value's label.'''
        return self._label

class VariableLabel:
    def __init__(self, variable_name, variable_label, value_labels=None):
        self._name= variable_name
        self._label= variable_label
        self._value_labels= value_labels

    @property
    def name(self):
        '''Read-only accessor to the variable's name.'''
        return self._name

    @property
    def label(self):
        '''Read-only accessor to the variable's label.'''
        return self._label

    @property
    def value_labels(self):
        '''Read-only accessor to any associated value labels.'''
        return self._value_labels


class VariableMetadata(namedtuple('_VariableMetadata', 'name, label, value_mappings')):
    '''
    A :py:class:`VariableMetadata` object contains the metadata about an
    individual form variable. The class inherits from a semi-anonymous
    :py:func:`namedtuple` (:py:class:`_VariableMetadata`) that handles object
    construction and the creation of immutable attribute accessors.

    :param str name: The encoded name of the variable (e.g. "a01")
    :param str label: The variable's readable label (e.g. "What is your sex?")
    :param dict value_mappings: A dictionary that maps encoded value names (e.g. "0", "1") to value labels (e.g. "Female", "Male")
    '''


    def _to_spss_syntax(self):
        '''
        Output the syntax file lines that correspond to this object.

        :returns: SPSS-syntax-file-formatted strings for use in a syntax file's "VARIABLE LABELS" and (possibly) "VALUE LABELS" sections.
        :rtype: tuple(str, str)
        '''

        spss_variable_name= get_spss_variable_name(self.name)

        if self.label is None:
            variable_label_line= None
        else:
            spss_variable_label= get_spss_variable_label(self.label)
            # Repeat any double quote characters found in the label.
            spss_variable_label= spss_variable_label.replace('"', '""')

            variable_label_line= INDENT_STRING + '/ ' + spss_variable_name + ' "' + spss_variable_label + '"'

        # There aren't always value labels to report.
        if self.value_mappings is None:
            value_label_lines= None
        else:
            value_label_lines= INDENT_STRING + '/ ' + spss_variable_name + '\n'

            sorted_value_names= self.value_mappings.keys()
            sorted_value_names.sort()
            for value_name in sorted_value_names:
                spss_value_label= get_spss_value_label(self.value_mappings[value_name])
                # Repeat any double quote characters found in the label.
                spss_value_label= spss_value_label.replace('"', '""')

                value_label_lines+= (INDENT_STRING * 2) + ' \'' + value_name + '\' "' + spss_value_label + '"'

        return variable_label_line, value_label_lines


    @classmethod
    def export_spss_syntax(cls, variable_metadata_list):
        '''
        Export the supplied :py:class:`VariableMetadata` objects to a string for
        use in an SPSS syntax file.

        :param variable_metadata_list: The metadata to export.
        :type variable_metadata_list: list(:py:class:`VariableMetadata`)
        :returns: An SPSS-syntax-file-formatted string.
        :rtype: :py:class:`String`
        '''

        if len(variable_metadata_list) == 0:
            return ''

        variable_label_lines= list()
        value_label_lines= list()
        for var_metadata in variable_metadata_list:
            var_label_line,  val_label_line= var_metadata._to_spss_syntax()
            if var_label_line != None:
                variable_label_lines.append(var_label_line)
            if val_label_line != None:
                value_label_lines.append(val_label_line)

        # Remove the prepending "/" from the first variable label and value label (if any) lines.
        variable_label_lines[0]= variable_label_lines[0].replace('/ ', '', 1)
        if value_label_lines:
            value_label_lines[0]= value_label_lines[0].replace('/ ', '', 1)

        syntax_string= VARIABLE_LABELS
        for var_label_line in variable_label_lines:
            syntax_string+= '\n' + var_label_line
        syntax_string+= '.\n'

        # There aren't always value labels to report.
        if len(value_label_lines) != 0:
            syntax_string+= '\n' + VALUE_LABELS
            for val_label_line in value_label_lines:
                syntax_string+= '\n' + val_label_line
            syntax_string+= '.\n'

        return syntax_string


    @classmethod
    def import_dicts(cls, variable_labels_dict, value_labels_dict):
        variable_metadata_list= list()

        if variable_labels_dict is None:
            variable_labels_dict= dict()
        if value_labels_dict is None:
            value_labels_dict= dict()

        for variable_name, variable_label in variable_labels_dict.iteritems():
            variable_metadata_list.append(cls(variable_name, variable_label, value_labels_dict.get(variable_name)))

        unlabeled_variables= set(value_labels_dict.keys()).difference(set(variable_labels_dict.keys()))
        for variable_name in unlabeled_variables:
            variable_metadata_list.append(cls(variable_name, None, value_labels_dict.get(variable_name)))

        return variable_metadata_list


    @classmethod
    def import_json(cls, odk_json_text):
        '''
        Parse question metadata (e.g. names, labels, value mappings) from the
        supplied JSON-formatted ODK form text.

        :param str odk_json_text: The JSON-formatted text of the form being imported.
        :returns: :py:class:`VariableMetadata` objects that correspond to the JSON form's questions.
        :rtype: list(:py:class:`VariableMetadata`)
        '''

        form_dict= json.loads(odk_json_text)
        return cls._import(form_dict)


    @classmethod
    def _import(cls, odk_form_dict):
        '''
        Where the actual importing work occurs. Takes an ODK form pre-parsed
        into :py:class:`dict` and generates the appropriate metadata.
        returns the appropriate :py:class:`VariableMetadata` objects.

        :param dict odk_form_dict: The ODK form parsed into a :py:class:`dict`.
        :returns: :py:class:`VariableMetadata` objects that correspond to the form's questions.
        :rtype: list(:py:class:`VariableMetadata`)
        '''

        form_variables= odk_form_dict['children']
        variable_metadata_list= list()
        for form_var in form_variables:
            if form_var['type'] == 'group':
                # Recursively import groups.
                group_variable_metadata_list= cls._import(form_var)
                variable_metadata_list.extend(group_variable_metadata_list)
                continue

            var_name= form_var['name'].encode('utf-8')
            if 'label' not in form_var.keys():
                var_label= None
            else:
                var_label= form_var['label'].encode('utf-8')

            # TODO: Find out multi-select "type" (e.g. "select multiple")
            if form_var['type'] in ['select one']:
                value_mappings_list= form_var['children']
                value_mappings= dict()
                for mapping in value_mappings_list:
                    val_name= mapping['name'].encode('utf-8')
                    val_label= mapping['label'].encode('utf-8')
                    value_mappings[val_name]= val_label
            else:
                value_mappings= None

            variable_metadata= cls(var_name, var_label, value_mappings)
            variable_metadata_list.append(variable_metadata)

            # TODO: Not really knowing the "calculate" syntax, this is likely very brittle.
            if form_var['type'] == 'calculate':
                calculation_string= form_var['bind']['calculate']
                # Find the first substring of the form "'matched substring:"
                calculated_var_name= re.match(r'''^.+'(.+):''', calculation_string).groups()[0].encode('utf-8')
                calculated_variable_metadata= cls(calculated_var_name, calculated_var_name, None)
                variable_metadata_list.append(calculated_variable_metadata)

        return variable_metadata_list
