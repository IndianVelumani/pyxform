from __future__ import unicode_literals

from pyxform import constants
from pyxform.question_type_dictionary import QUESTION_TYPE_DICT
from pyxform.errors import PyXFormError


# Aliases:
# Ideally aliases should resolve to elements in the json form schema

# select, control and settings alias keys used for parsing,
# which is why self mapped keys are necessary.

control = {
    constants.GROUP: constants.GROUP,
    'lgroup': constants.REPEAT,
    constants.REPEAT: constants.REPEAT,
    constants.LOOP: constants.LOOP,
    'looped group': constants.REPEAT
}

select_one = {
    constants.SELECT_ONE:                               constants.SELECT_ONE,
    constants.SELECT_ONE_XLSFORM:                       constants.SELECT_ONE,
    constants.SELECT_ONE_XFORM:                         constants.SELECT_ONE,
    'select one from':                                  constants.SELECT_ONE,
    'add select one prompt using':                      constants.SELECT_ONE,
    # 'select_one_from_file'
    constants.SELECT_ONE_XLSFORM + '_from_file':        constants.SELECT_ONE,
    # 'select one from file'
    constants.SELECT_ONE + ' from file':                constants.SELECT_ONE,
}

select_multiple = {
    constants.SELECT_ALL_THAT_APPLY:            constants.SELECT_ALL_THAT_APPLY,
    constants.SELECT_ALL_THAT_APPLY_XLSFORM:    constants.SELECT_ALL_THAT_APPLY,
    constants.SELECT_ALL_THAT_APPLY_XFORM:      constants.SELECT_ALL_THAT_APPLY,
    # 'select all that apply from'
    constants.SELECT_ALL_THAT_APPLY + ' from':  constants.SELECT_ALL_THAT_APPLY,
    'add select multiple prompt using':         constants.SELECT_ALL_THAT_APPLY,
    'select multiple from file':                constants.SELECT_ALL_THAT_APPLY,
    'select_multiple_from_file':                constants.SELECT_ALL_THAT_APPLY,
}

select_one_external = {'select_one_external': 'select one external'}

select = dict()
select.update(select_one)
select.update(select_multiple)
select.update(select_one_external)

cascading = {
    'cascading select':         constants.CASCADING_SELECT,
    constants.CASCADING_SELECT: constants.CASCADING_SELECT,
}

settings_header = {
    'form_title':                   constants.TITLE,
    'set form title':               constants.TITLE,
    'form_id':                      constants.ID_STRING,
    constants.SMS_KEYWORD:          constants.SMS_KEYWORD,
    constants.SMS_SEPARATOR:        constants.SMS_SEPARATOR,
    constants.SMS_ALLOW_MEDIA:      constants.SMS_ALLOW_MEDIA,
    constants.SMS_DATE_FORMAT:      constants.SMS_DATE_FORMAT,
    constants.SMS_DATETIME_FORMAT:  constants.SMS_DATETIME_FORMAT,
    'set form id':                  constants.ID_STRING,
    constants.PUBLIC_KEY:           constants.PUBLIC_KEY,
    constants.SUBMISSION_URL:       constants.SUBMISSION_URL
}

# TODO: Check on bind prefix approach in json.
# Conversion dictionary from user friendly column names to meaningful values
survey_header = {
    'Label':                    constants.LABEL,
    'Name':                     constants.NAME,
    'SMS Field':                constants.SMS_FIELD,
    'SMS Option':               constants.SMS_OPTION,
    'SMS Sepatator':            constants.SMS_SEPARATOR,
    'SMS Allow Media':          constants.SMS_ALLOW_MEDIA,
    'SMS Date Format':          constants.SMS_DATE_FORMAT,
    'SMS DateTime Format':      constants.SMS_DATETIME_FORMAT,
    'SMS Response':             constants.SMS_RESPONSE,
    'Type':                     constants.TYPE,
    'List_name':                'list_name',
    # u"repeat_count": u"jr:count",  duplicate key
    'read_only':                constants.BIND + '::readonly',
    'readonly':                 constants.BIND + '::readonly',
    'relevant':                 constants.BIND + '::relevant',
    'caption':                  constants.LABEL,
    constants.APPEARANCE:       constants.CONTROL + '::' + constants.APPEARANCE,  # TODO: this is also an issue
    'relevance':                constants.BIND + '::relevant',
    'required':                 constants.BIND + '::required',
    'constraint':               constants.BIND + '::constraint',
    'constraining message':     constants.BIND + '::jr:constraintMsg',
    'constraint message':       constants.BIND + '::jr:constraintMsg',
    'constraint_message':       constants.BIND + '::jr:constraintMsg',
    'calculation':              constants.BIND + '::' + constants.CALCULATE_XFORM,
    'command':                  constants.TYPE,
    'tag':                      constants.NAME,
    'value':                    constants.NAME,
    constants.IMAGE_XLSFORM:    constants.MEDIA + '::' + constants.IMAGE_XLSFORM,
    constants.AUDIO_XLSFORM:    constants.MEDIA + '::' + constants.AUDIO_XLSFORM,
    constants.VIDEO_XLSFORM:    constants.MEDIA + '::' + constants.VIDEO_XLSFORM,
    'count':                    constants.CONTROL + '::jr:count',
    'repeat_count':             constants.CONTROL + '::jr:count',
    'jr:count':                 constants.CONTROL + '::jr:count',
    'autoplay':                 constants.CONTROL + '::autoplay',
    'rows':                     constants.CONTROL + '::rows',
    # New elements that have to go into itext elements:
    'noAppErrorString':         constants.BIND + '::jr:noAppErrorString',
    'no_app_error_string':      constants.BIND + '::jr:noAppErrorString',
    'requiredMsg':              constants.BIND + '::jr:requiredMsg',
    'required message':         constants.BIND + '::jr:requiredMsg',
    'required_message':         constants.BIND + '::jr:requiredMsg',
    constants.BODY_XFORM:       constants.CONTROL,
}

list_header = {
    'caption':                  constants.LABEL,
    'list_name':                constants.LIST_NAME,
    'value':                    constants.NAME,
    constants.IMAGE_XLSFORM:    constants.MEDIA + '::' + constants.IMAGE_XLSFORM,
    constants.AUDIO_XLSFORM:    constants.MEDIA + '::' + constants.AUDIO_XLSFORM,
    constants.VIDEO_XLSFORM:    constants.MEDIA + '::' + constants.VIDEO_XLSFORM,
}

# Note that most of the type aliasing happens in all.xls
_type = {
    'imei':                                         constants.DEVICEID_XLSFORM,
    constants.IMAGE_XLSFORM:                        'photo',
    'add ' + constants.IMAGE_XLSFORM + ' prompt':   'photo',
    'add ' + constants.AUDIO_XLSFORM + ' prompt':   constants.AUDIO_XLSFORM,
    'add ' + constants.VIDEO_XLSFORM + ' prompt':   constants.VIDEO_XLSFORM,
    'add photo prompt':                             'photo',
    'add file prompt':                               'file'
}

yes_no = {
    'yes':      True,
    'Yes':      True,
    'YES':      True,
    'true':     True,
    'True':     True,
    'TRUE':     True,
    'true()':   True,
    'no':       False,
    'No':       False,
    'NO':       False,
    'false':    False,
    'False':    False,
    'FALSE':    False,
    'false()':  False,
}

label_optional_types = [
    constants.DEVICEID_XLSFORM,
    constants.PHONENUMBER_XLSFORM,
    constants.SIMSERIAL_XLSFORM,
    constants.CALCULATE_XFORM,  # Not `constants.CALCULATE_XLSFORM`?
    constants.START_XLSFORM,
    constants.END_XLSFORM,
    constants.TODAY_XLSFORM,
]

osm = {
    'osm': constants.OSM_TYPE
}


def get_xform_question_type(original_question_type_str):
    '''
    Determine the XForm-compatible question type that corresponds to the given type.

    :param str original_question_type_str:
    :return: An XForm-compatible question type.
    :rtype: str
    '''

    xform_question_type_str= None

    # Strip off the "xsd:" prefix, if present.
    if original_question_type_str.startswith('xsd:'):
        question_type_str= original_question_type_str.split('xsd:')[-1]
    else:
        question_type_str= original_question_type_str

    if question_type_str in select_one:
        xform_question_type_str= constants.SELECT_ONE_XFORM
    elif question_type_str in select_multiple:
        xform_question_type_str= constants.SELECT_ALL_THAT_APPLY_XFORM
    elif question_type_str in constants.XFORM_TYPES:
        # The question type is already valid for use in an XForm.
        xform_question_type_str= question_type_str

    elif question_type_str in constants.XLSFORM_TO_XFORM_TYPES:
        # The question type is an XLSForm type with a known XForm equivalent.
        xform_question_type_str= constants.XLSFORM_TO_XFORM_TYPES[question_type_str]

    elif question_type_str in QUESTION_TYPE_DICT:
        # The question type is a known type possibly with an XForm equivalent.
        possible_xform_question_type= \
            QUESTION_TYPE_DICT[question_type_str][constants.BIND][constants.TYPE]
        if possible_xform_question_type in constants.XFORM_TYPES:
            xform_question_type_str= possible_xform_question_type
    elif question_type_str == constants.GROUP:
        xform_question_type_str= question_type_str

    if not xform_question_type_str:
        raise PyXFormError('Could not find XForm equivalent of type "{}".'
                           .format(question_type_str))

    return xform_question_type_str


def get_xlsform_question_type(original_question_type_str):
    '''
    Determine the XLSForm-compatible question type that corresponds to the given type.

    :param str original_question_type_str:
    :return: An XLSForm-compatible question type.
    :rtype: str
    '''

    xlsform_question_type_str= None

    if original_question_type_str in \
            set(constants.XLSFORM_TYPES).union(constants.XLSFORM_METADATA_TYPES):
        # The question type is already valid for use in an XLSForm.
        xlsform_question_type_str= original_question_type_str

    elif original_question_type_str in constants.XFORM_TO_XLSFORM_TYPES:
        # The question type is an XForm type with a known XLSForm equivalent.
        xlsform_question_type_str= constants.XFORM_TO_XLSFORM_TYPES[original_question_type_str]

    elif original_question_type_str == constants.GROUP:
        xlsform_question_type_str= original_question_type_str
    else:
        # FIXME: This wouldn't be necessary if 'Question' internally standardized \
        #   to use types from the XForm (or alternatively XLSForm) spec.
        xform_question_type= get_xform_question_type(original_question_type_str)
        if xform_question_type in constants.XFORM_TO_XLSFORM_TYPES:
            xlsform_question_type_str= constants.XFORM_TO_XLSFORM_TYPES[xform_question_type]

    if not xlsform_question_type_str:
        raise PyXFormError('Could not find XLSForm equivalent of type "{}".'
                           .format(original_question_type_str))
    else:
        return xlsform_question_type_str
