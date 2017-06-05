'''
Created on Jan 21, 2015

@author: esmail
'''


from __future__ import unicode_literals

import io
from collections import OrderedDict

from .utilities import get_spss_variable_name
from . import from_dicts

from .. import constants
from ..utilities.get_label_mappings import get_label_mappings
from ..survey import Survey
import zipfile


VARIABLE_LABELS_DICT_KEY, VALUE_LABELS_DICT_KEY= 'variable_labels_dict', 'value_labels_dict'


def question_to_spss_variable_name(question, group_delimiter=None):
    group_prefix= ''
    if group_delimiter is not None:
        # If the question's full path is desired, find it.
        parent= question.get(constants.PARENT, Survey())
        while not isinstance(parent, Survey):
            group_prefix= parent.name + group_delimiter + group_prefix
            parent= parent.get(constants.PARENT, Survey())

    if question.is_multi_select():
        # FIXME: This kind of overloading is dangerous; find a better interface.
        # Actually return a list of the names of the SPSS variables this multi-select will be disaggregated into.
        base_variable_name= group_prefix + question.name
        spss_variable_name= [get_spss_variable_name(base_variable_name)]

        for option in question.options:
            disaggregated_variable_name= get_spss_variable_name(base_variable_name + option.name)
            spss_variable_name.append(disaggregated_variable_name)
    else:
        spss_variable_name= get_spss_variable_name(group_prefix + question.name)

    return spss_variable_name


def get_per_language_labels(survey, path_prefixes=True, question_name_transform=None):

    # Get all question and option labels and all languages represented in the labels.
    question_label_mappings, option_label_mappings, label_languages= get_label_mappings(survey, path_prefixes=path_prefixes)

    # Organize the labels by language
    per_language_labels= dict()
    for question_name, question_labels in question_label_mappings.iteritems():

        if question_name_transform:
            final_question_name= question_name_transform(question_name)
        else:
            final_question_name= question_name
        question_options= option_label_mappings.get(question_name, dict())

        for language in label_languages:
            if language in question_labels:
                per_language_labels.setdefault(language, dict()).setdefault(VARIABLE_LABELS_DICT_KEY, OrderedDict())[final_question_name]= question_labels[language]

            for option_name, option_labels in question_options.iteritems():
                if language in option_labels:
                    per_language_labels.setdefault(language, dict()).setdefault(VALUE_LABELS_DICT_KEY, OrderedDict()).setdefault(final_question_name, OrderedDict())[option_name]= option_labels[language]

    return per_language_labels


def survey_to_spss_label_syntaxes(survey):
    '''
    Generate SPSS label syntax content for each language of the given survey.

    :param Survey survey: The survey from which the SPSS label syntaxes will be generated.
    :returns: A mapping from languages to SPSS label syntaxes.
    :rytpe: dict[basestring, basestring]
    '''

    exportable_label_mappings= get_per_language_labels(survey)

    syntaxes= dict()
    for language in exportable_label_mappings.keys():
        variable_labels_dict= exportable_label_mappings.get(language, dict()).get(
            VARIABLE_LABELS_DICT_KEY)
        value_labels_dict= exportable_label_mappings.get(language, dict()).get(
            VALUE_LABELS_DICT_KEY)

        spss_label_syntax_string= from_dicts(variable_labels_dict, value_labels_dict)
        syntaxes[language]= spss_label_syntax_string

    return syntaxes


def survey_to_spss_label_zip(survey, base_name):
    '''
    Generate a zip file containing SPSS label syntax files for each language in the given survey.

    :param Survey survey: The survey from which the syntax file(s) will be generated.
    :param basestring base_name: The base for the syntax file filename(s).
    :return: An in-memory zip file containing all generated syntax files.
    :rtype: io.BytesIO
    '''

    syntaxes= survey_to_spss_label_syntaxes(survey)
    zip_io= io.BytesIO()
    with zipfile.ZipFile(zip_io, 'w', compression=zipfile.ZIP_DEFLATED) as zip_out_zipfile:
        for language, syntax_file_contents in syntaxes.iteritems():
            syntax_file_name= '{}_{}_labels.sps'.format(base_name, language)
            zip_out_zipfile.writestr(syntax_file_name, syntax_file_contents.encode('UTF-8'))

    zip_io.seek(0)
    return zip_io


# TODO: Does this maybe belong in KoBoCAT?
def get_multi_select_disaggregated_question_names(question, group_delimiter='/'):
    '''
    Get a list of the question names a multi-select question's options will be
    disaggregated into when exported.
    '''

    assert question.is_multi_select()
    base_question_name= question.get_path()

    disaggregated_question_names= list()
    for option in question.options:
        disaggregated_question_names.append(base_question_name + group_delimiter + option.name)

    return disaggregated_question_names

