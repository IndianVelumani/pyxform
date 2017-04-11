"""
This file contains constants that correspond with the property names in the
json survey format. (@see json_form_schema.json) These names are to be shared
between X2json and json2Y programs. By putting them in a shared file,
the literal names can be easily changed, typos can be avoided, and references
are easier to find.
"""

from __future__ import unicode_literals


TITLE =                     'title'
NAME =                      'name'
ID_STRING =                 'id_string'
SMS_KEYWORD =               'sms_keyword'
SMS_FIELD =                 'sms_field'
SMS_OPTION =                'sms_option'
SMS_SEPARATOR =             'sms_separator'
SMS_ALLOW_MEDIA =           'sms_allow_media'
SMS_DATE_FORMAT =           'sms_date_format'
SMS_DATETIME_FORMAT =       'sms_datetime_format'
SMS_RESPONSE =              'sms_response'
VERSION =                   'version'
PUBLIC_KEY =                'public_key'
SUBMISSION_URL =            'submission_url'
DEFAULT_LANGUAGE =          'default_language'
ACTUAL_DEFAULT_LANGUAGE=    'default'
STYLE =                     'style'
ATTRIBUTE =                 'attribute'

BIND =          'bind'  # TODO: What should I do with the nested types? (readonly and relevant) # noqa
MEDIA =         'media'
CONTROL =       'control'
APPEARANCE =    'appearance'

LOOP =      'loop'
COLUMNS =   'columns'

CHILDREN =      'children'
PARENT=         'parent'
MODEL_XFORM=    'model'
BODY_XFORM=     'body'
INSTANCE_XFORM= 'instance'
META_XFORM=     'meta'
REF_XFORM=      'ref'


# XFrom bind attributes: http://opendatakit.github.io/odk-xform-spec/#bind-attributes.
NODESET_XFORM=          'nodeset'
TYPE =                  'type'
READONLY_XFORM=         'readonly'
REQUIRED_XFORM=         'required'
RELEVANT_XFORM=         'relevant'
CALCULATE_XFORM=        'calculate'
CONSTRAINT_XFORM=       'constraint'
CONSTRAINT_MSG_XFORM=   'jr:constraintMsg'
PRELOAD_XFORM=          'jr:preload'
PRELOAD_PARAMS_XFORM=   'jr:preloadParams'

BIND_ATTRIBUTES_XFORM= {NODESET_XFORM, TYPE, READONLY_XFORM, REQUIRED_XFORM,
                        RELEVANT_XFORM, CALCULATE_XFORM, CONSTRAINT_XFORM, CONSTRAINT_MSG_XFORM,
                        PRELOAD_XFORM, PRELOAD_PARAMS_XFORM}


# Question/data types.
# ODK XForm data types: http://opendatakit.github.io/odk-xform-spec/#data-types.
# XLSForm question types: http://xlsform.org/#question%20types.
STRING_XFORM=   'string'
STRING_XLSFORM= 'text'

INT_XFORM=      'int'
INT_XLSFORM=    'integer'

BOOLEAN_XFORM= 'boolean'
# Presumably boolean questions are represented as "select one" questions in XLSForms.

DECIMAL_XFORM=      'decimal'
DECIMAL_XLSFORM=    DECIMAL_XFORM

DATE_XFORM=     'date'
DATE_XLSFORM=   DATE_XFORM

TIME_XFORM=     'time'
TIME_XLSFORM=   TIME_XFORM

DATETIME_XFORM=     'dateTime'
DATETIME_XLSFORM=   DATETIME_XFORM

SELECT_ALL_THAT_APPLY_XFORM=    'select'
SELECT_ALL_THAT_APPLY_XLSFORM=  'select_multiple'
SELECT_ALL_THAT_APPLY =         'select all that apply'

SELECT_ONE_XFORM=   'select1'
SELECT_ONE_XLSFORM= 'select_one'
SELECT_ONE =        'select one'

GEOPOINT_XFORM=     'geopoint'
GEOPOINT_XLSFORM=   GEOPOINT_XFORM

GEOTRACE_XFORM= 'geotrace'

GEOSHAPE_XFORM= 'geoshape'

BINARY_XFORM=   'binary'
IMAGE_XLSFORM=  'image'
AUDIO_XLSFORM=  'audio'
VIDEO_XLSFORM=  'video'

BARCODE_XFORM=      'barcode'
BARCODE_XLSFORM=    BARCODE_XFORM

NOTE_XLSFORM= 'note'

CALCULATE_XLSFORM= 'calculation'

TRIGGER_XLSFORM= 'acknowledge'

XFORM_TYPES= {STRING_XFORM, INT_XFORM, BOOLEAN_XFORM, DECIMAL_XFORM, DATE_XFORM,
              TIME_XFORM, DATETIME_XFORM, SELECT_ALL_THAT_APPLY_XFORM, SELECT_ONE_XFORM,
              GEOPOINT_XFORM, GEOTRACE_XFORM, GEOSHAPE_XFORM, BINARY_XFORM, BARCODE_XFORM}

XLSFORM_TYPES= {STRING_XLSFORM, INT_XLSFORM, DECIMAL_XLSFORM, DATE_XLSFORM, TIME_XLSFORM,
                DATETIME_XLSFORM, SELECT_ALL_THAT_APPLY_XLSFORM, SELECT_ONE_XLSFORM,
                GEOPOINT_XLSFORM, IMAGE_XLSFORM, AUDIO_XLSFORM, VIDEO_XLSFORM, BARCODE_XLSFORM,
                NOTE_XLSFORM, CALCULATE_XLSFORM, TRIGGER_XLSFORM}

XFORM_TO_XLSFORM_TYPES= {
    STRING_XFORM:                   STRING_XLSFORM,
    INT_XFORM:                      INT_XLSFORM,
#     BOOLEAN_XFORM: None,
    DECIMAL_XFORM:                  DECIMAL_XLSFORM,
    DATE_XFORM:                     DATE_XLSFORM,
    TIME_XFORM:                     TIME_XLSFORM,
    DATETIME_XFORM:                 DATETIME_XLSFORM,
    SELECT_ALL_THAT_APPLY_XFORM:    SELECT_ALL_THAT_APPLY_XLSFORM,
    SELECT_ONE_XFORM:               SELECT_ONE_XLSFORM,
    GEOPOINT_XFORM:                 GEOPOINT_XLSFORM,
#     GEOTRACE_XFORM: None,
#     GEOSHAPE_XFORM: None,
#     BINARY_XFORM: [IMAGE_XLSFORM, AUDIO_XLSFORM, VIDEO_XLSFORM],
    BARCODE_XFORM:                  BARCODE_XFORM,
}

XLSFORM_TO_XFORM_TYPES= {xlsform_type: xform_type 
                         for xform_type, xlsform_type in XFORM_TO_XLSFORM_TYPES.iteritems()}


# Metadata types: http://xlsform.org/#metadata
START_XLSFORM=          'start'
END_XLSFORM=            'end'
TODAY_XLSFORM=          'today'
DEVICEID_XLSFORM=       'deviceid'
SUBSCRIBERID_XLSFORM=   'subscriberid'
SIMSERIAL_XLSFORM=      'simserial'
PHONENUMBER_XLSFORM=    'phonenumber'

XLSFORM_METADATA_TYPES= {START_XLSFORM, END_XLSFORM, TODAY_XLSFORM, DEVICEID_XLSFORM, 
                         SUBSCRIBERID_XLSFORM, SIMSERIAL_XLSFORM, PHONENUMBER_XLSFORM}


# XForm body elements: http://opendatakit.github.io/odk-xform-spec/#body-elements
INPUT_XFORM=    'input'
UPLOAD_XFORM=   'upload'
TRIGGER_XFORM=  'trigger'
GROUP =         'group'
REPEAT =        'repeat'

XFORM_BODY_ELEMENTS= {INPUT_XFORM, SELECT_ONE_XFORM, SELECT_ALL_THAT_APPLY_XFORM, UPLOAD_XFORM, 
                      TRIGGER_XFORM, GROUP, REPEAT}

# Special body element types that are also question types (?).
XFORM_TYPE_BODY_ELEMENTS= {SELECT_ONE_XFORM, SELECT_ALL_THAT_APPLY_XFORM, TRIGGER_XFORM}


# XForm body sub-elements: http://opendatakit.github.io/odk-xform-spec/#body-elements
HINT =          'hint'
LABEL =         'label'
OUTOPUT_XFORM=  'output'
ITEM_XFORM=     'item'
ITEMSET_XFORM=  'itemset'
VALUE_XFORM=    'value'

# XLS Specific constants
LIST_NAME =         'list name'
CASCADING_SELECT =  'cascading_select'
TABLE_LIST =        'table-list'  # hyphenated because it goes in appearance, and convention for appearance column is dashes # noqa

# The following are the possible sheet names:
SURVEY =    'survey'
SETTINGS =  'settings'
CHOICES =   'choices'

# These sheet names are for list sheets
CHOICES_AND_COLUMNS =   'choices and columns'
CASCADING_CHOICES =     'cascades'

OSM =       'osm'
OSM_TYPE =  'binary'

NAMESPACES = 'namespaces'

