'''
Created on May 8, 2015

@author: esmail
'''


import re
import unittest
import zipfile
from collections import OrderedDict

from .pyxform_test_case import PyxformTestCase
from ..constants import ACTUAL_DEFAULT_LANGUAGE
from ..spss.spss import get_per_language_labels
from ..spss.spss import survey_to_spss_label_syntaxes
from ..spss.spss import survey_to_spss_label_zip
from ..spss.spss import VALUE_LABELS_DICT_KEY
from ..spss.spss import VARIABLE_LABELS_DICT_KEY
from ..spss.utilities import get_spss_variable_name
from ..spss.variable_metadata import VALUE_LABELS
from ..spss.variable_metadata import VARIABLE_LABELS


class TestSpssLabelSyntax(PyxformTestCase):

    @classmethod
    def setUpClass(cls):
        md= \
        '''
        | survey  |                    |        |                    |                            |
        |         | type               | name   | label              | label:English              |
        |         | text               | q1     | Q1                 | Q1 English                 |
        |         | integer            | q2     | Q2                 |                            |
        |         | decimal            | q3     |                    | Q3 English                 |
        |         | select_one so1     | q4     | Q4                 | Q4 English                 |
        |         | select_multiple sm | q5     | Q5                 | Q5 English                 |
        |         | select_one so2     | q6     | Q6                 | Q6 English                 |
        |         |                    |        |                    |                            |
        | choices |                    |        |                    |                            |
        |         | list name          | name   | label              | label:English              |
        |         | so1                | so1_o1 | Select one Q4 O1   | Select one Q4 O1 English   |
        |         | so1                | so1_o2 | Select one Q4 O2   |                            |
        |         | so1                | so1_o3 |                    | Select one Q4 O3 English   |
        |         | sm                 | sm_o1  | Select multiple O1 |                            |
        |         | sm                 | sm_o2  |                    | Select multiple O2 English |
        |         | so2                | so2_o1 | Select one Q6 O1   | Select one Q6 O1 English   |
        |         | so2                | so2_o2 | Select one Q6 O2   |                            |
        |         | so2                | so2_o3 |                    | Select one Q6 O3 English   |
        '''

        cls.survey = cls.md_to_pyxform_survey(md)
        cls.labels = get_per_language_labels(cls.survey,
                                             question_name_transform=get_spss_variable_name)

    def _variable_label_syntax_to_mappings(self, syntax):
        '''
        Parse variable label mappings from a SPSS syntax file's "VARIABLE LABELS" section.

        :param basestring syntax: SPSS syntax text.
        :return: A mapping from variable names to their labels.
        :rtype: OrderedDict[str, basestring]
        '''

        variable_label_syntax_content = re.compile(VARIABLE_LABELS + r'\n(.+?)\.\n',
                                                   flags=re.DOTALL).search(syntax).groups()[0]

        # Normalize first line to conform with the rest; e.g. ' / question_name "Question Label"'.
        variable_label_syntax_content = ' /' + variable_label_syntax_content

        # Extract the question ("variable") to label mappings.
        variable_labels = (re.compile(r'^\s*/\s+(\S+)\s+"(.*)"\s*$').search(line).groups()
                           for line in variable_label_syntax_content.splitlines())
        variable_labels = OrderedDict(variable_labels)

        # Variable names must be ASCII encoded and SPSS-compatible.
        variable_labels = {variable_name.encode('ASCII'): label
                           for variable_name, label in variable_labels.iteritems()}

        return variable_labels

    def _label_syntax_to_value_labels(self, syntax):
        '''
        Parse value label mappings from a SPSS syntax file's "VALUE LABELS" section.

        :param basestring syntax: SPSS syntax text.
        :return: A mapping from multiple_choice question names to mappings of the their values to
            their labels.
        :rtype: OrderedDict[OrderedDict[basestring, basestring]]
        '''

        value_label_syntax_content = re.search(VALUE_LABELS + r'\n(.+?)\.$', syntax,
                                               flags=re.DOTALL).groups()[0]

        # Normalize the first lines to e.g. " / q_name" by adding a initial "/".
        value_label_syntax_content = ' /' + value_label_syntax_content

        # Break the syntax down into per-question sections.
        remaining_syntax = value_label_syntax_content
        value_label_sections = list()
        section_regex = re.compile(r'\s*/\s+([^/]+?)($|\s*/)')
        while section_regex.search(remaining_syntax):
            split_results = section_regex.split(remaining_syntax, maxsplit=1)
            value_label_sections.append(split_results[1])
            remaining_syntax = ''.join(split_results[2:])

        value_labels = OrderedDict()
        for section in value_label_sections:
            _, variable_name, remaining_syntax = re.split(r'(\S+)\s+', section, maxsplit=1)
            value_label_mapping_regex = re.compile('''\s*'([^']+?)'\s+"(.+?)"\s*('|$)''')
            while value_label_mapping_regex.search(remaining_syntax):
                split_results = re.compile('''\s*'([^']+?)'\s+"(.+?)"\s*('|$)''').split(
                    remaining_syntax, maxsplit=1)
                value_name, value_label = split_results[1:3]
                value_labels.setdefault(variable_name, OrderedDict())[value_name] = value_label
                remaining_syntax = ''.join(split_results[3:])

        return value_labels

    def test_spss_label_syntaxes_generation(self, spss_label_syntaxes=None, expected_labels=None):
        '''
        Test the generated SPSS label syntax.

        :param dict[str, str] spss_label_syntaxes: SPSS label syntax strings organized by language.
        :param dict[str, str] expected_labels: Variable and/or value mappings organized by language.
        '''

        if spss_label_syntaxes is None:
            spss_label_syntaxes= survey_to_spss_label_syntaxes(self.survey)

        if expected_labels is None:
            expected_labels = self.labels

        languages= spss_label_syntaxes.keys()

        for language in languages:
            self.assertSetEqual(set(languages), set(expected_labels.iterkeys()))

            syntax = spss_label_syntaxes[language]

    def test_spss_label_zip_generation(self):
        spss_label_syntaxes= dict()
        base_name= 'some_base_name'
        zip_io= survey_to_spss_label_zip(self.survey, base_name)
        with zipfile.ZipFile(zip_io) as label_zipfile:
            languages= [ACTUAL_DEFAULT_LANGUAGE, 'English']
            for lang in languages:
                syntax_filename= '{}_{}_labels.sps'.format(base_name, lang)
                with label_zipfile.open(syntax_filename) as syntax_file:
                    spss_label_syntaxes[lang]= syntax_file.read()

        self.test_spss_label_syntaxes_generation(spss_label_syntaxes)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
