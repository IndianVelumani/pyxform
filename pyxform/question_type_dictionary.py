from xls2json import QuestionTypesReader, print_pyobj_to_json
from pyxform import constants

FILE_MEDIA_TYPES = ",".join([
    "text/plain",
    "application/pdf",
    "application/vnd.ms-excel",
    "application/msword",
    "text/richtext",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    "application/zip",
    "application/x-zip",
    "application/x-zip-compressed"
])


def generate_new_dict():
    """
    This is just here incase there is ever any need to generate the question
    type dictionary from all.xls again.
    It shouldn't be called as part of any application.
    """
    path_to_question_types = "/home/nathan/aptana-workspace/pyxform"\
        "/pyxform/question_types/all.xls"
    json_dict = QuestionTypesReader(path_to_question_types).to_json_dict()
    print_pyobj_to_json(json_dict, 'new_quesiton_type_dict.json')

_SELECT_1_TYPE_DICT= {
    "control": {
        "tag": constants.SELECT_ONE_XFORM
    }, 
    "bind": {
        "type": constants.SELECT_ONE_XFORM
    }
}

_SELECT_TYPE_DICT= {
    "control": {
        "tag": constants.SELECT_ALL_THAT_APPLY_XFORM
    }, 
    "bind": {
        "type": constants.SELECT_ALL_THAT_APPLY_XFORM
    }
}

QUESTION_TYPE_DICT = \
{
    "q picture": {
        "control": {
            "tag": "upload", 
            "mediatype": "image/*"
        }, 
        "bind": {
            "type": "binary"
        }
    }, 
    "photo": {
        "control": {
            "tag": "upload", 
            "mediatype": "image/*"
        }, 
        "bind": {
            "type": "binary"
        }
    }, 
    "add date time prompt": {
        "control": {
            "tag": "input"
        }, 
        "bind": {
            "type": "dateTime"
        }
    }, 
    "add audio prompt": {
        "control": {
            "tag": "upload", 
            "mediatype": "audio/*"
        }, 
        "bind": {
            "type": "binary"
        }
    }, 
    "q date time": {
        "control": {
            "tag": "input"
        }, 
        "bind": {
            "type": "dateTime"
        }
    }, 
    "phonenumber": {
        "bind": {
            "jr:preload": "property", 
            "type": "string", 
            "jr:preloadParams": "phonenumber"
        }
    }, 
    "get start time": {
        "bind": {
            "jr:preload": "timestamp", 
            "type": "dateTime", 
            "jr:preloadParams": "start"
        }
    }, 
    "add note prompt": {
        "control": {
            "tag": "input"
        }, 
        "bind": {
            "readonly": "true()", 
            "type": "string"
        }
    }, 
    "calculate": {
        "bind": {
            "type": "string"
        }
    }, 
    "acknowledge": {
        "control": {
            "tag": "trigger"
        }, 
        "bind": {
            "type": "string"
        }
    }, 
    "location": {
        "control": {
            "tag": "input"
        }, 
        "bind": {
            "type": "geopoint"
        }
    }, 
    "text": {
        "control": {
            "tag": "input"
        }, 
        "bind": {
            "type": "string"
        }
    }, 
    "simserial": {
        "bind": {
            "jr:preload": "property", 
            "type": "string", 
            "jr:preloadParams": "simserial"
        }
    }, 
    "string": {
        "control": {
            "tag": "input"
        }, 
        "bind": {
            "type": "string"
        }
    }, 
    "q string": {
        "control": {
            "tag": "input"
        }, 
        "bind": {
            "type": "string"
        }
    }, 
    "imei": {
        "bind": {
            "jr:preload": "property", 
            "type": "string", 
            "jr:preloadParams": "deviceid"
        }
    }, 
    "integer": {
        "control": {
            "tag": "input"
        }, 
        "bind": {
            "type": "int"
        }
    }, 
    "datetime": {
        "control": {
            "tag": "input"
        }, 
        "bind": {
            "type": "dateTime"
        }
    }, 
    "q note": {
        "control": {
            "tag": "input"
        }, 
        "bind": {
            "readonly": "true()", 
            "type": "string"
        }
    }, 
    "subscriber id": {
        "bind": {
            "jr:preload": "property", 
            "type": "string", 
            "jr:preloadParams": "subscriberid"
        }
    }, 
    "decimal": {
        "control": {
            "tag": "input"
        }, 
        "bind": {
            "type": "decimal"
        }
    }, 
    "dateTime": {
        "control": {
            "tag": "input"
        }, 
        "bind": {
            "type": "dateTime"
        }
    }, 
    "q audio": {
        "control": {
            "tag": "upload", 
            "mediatype": "audio/*"
        }, 
        "bind": {
            "type": "binary"
        }
    }, 
    "q geopoint": {
        "control": {
            "tag": "input"
        }, 
        "bind": {
            "type": "geopoint"
        }
    }, 
    "q geoshape": {
        "control": {
            "tag": "input"
        }, 
        "bind": {
            "type": "geoshape"
        }
    }, 
    "q geotrace": {
        "control": {
            "tag": "input"
        }, 
        "bind": {
            "type": "geotrace"
        }
    }, 
    "q image": {
        "control": {
            "tag": "upload", 
            "mediatype": "image/*"
        }, 
        "bind": {
            "type": "binary"
        }
    }, 
    "get today": {
        "bind": {
            "jr:preload": "date", 
            "type": "date", 
            "jr:preloadParams": "today"
        }
    }, 
    "video": {
        "control": {
            "tag": "upload", 
            "mediatype": "video/*"
        }, 
        "bind": {
            "type": "binary"
        }
    }, 
    "q acknowledge": {
        "control": {
            "tag": "trigger"
        }, 
        "bind": {
            "type": "string"
        }
    }, 
    "add video prompt": {
        "control": {
            "tag": "upload", 
            "mediatype": "video/*"
        }, 
        "bind": {
            "type": "binary"
        }
    }, 
    "number of days in last month": {
        "control": {
            "tag": "input"
        }, 
        "bind": {
            "type": "int", 
            "constraint": "0 <= . and . <= 31"
        }, 
        "hint": "Enter a number 0-31."
    }, 
    "get sim id": {
        "bind": {
            "jr:preload": "property", 
            "type": "string", 
            "jr:preloadParams": "simserial"
        }
    }, 
    "q location": {
        "control": {
            "tag": "input"
        }, 
        "bind": {
            "type": "geopoint"
        }
    }, 
    "select one external": {
        "control": {
            "tag": "input"
        }, 
        "bind": {
            "type": "string"
        }
    }, 
    "add image prompt": {
        "control": {
            "tag": "upload", 
            "mediatype": "image/*"
        }, 
        "bind": {
            "type": "binary"
        }
    }, 
    "get end time": {
        "bind": {
            "jr:preload": "timestamp", 
            "type": "dateTime", 
            "jr:preloadParams": "end"
        }
    }, 
    "barcode": {
        "control": {
            "tag": "input"
        }, 
        "bind": {
            "type": "barcode"
        }
    }, 
    "q video": {
        "control": {
            "tag": "upload", 
            "mediatype": "video/*"
        }, 
        "bind": {
            "type": "binary"
        }
    }, 
    "geopoint": {
        "control": {
            "tag": "input"
        }, 
        "bind": {
            "type": "geopoint"
        }, 
        "hint": "GPS coordinates can only be collected when outside."
    }, 
    "geoshape": {
        "control": {
            "tag": "input"
        }, 
        "bind": {
            "type": "geoshape"
        }, 
        "hint": "GPS coordinates can only be collected when outside."
    }, 
    "geotrace": {
        "control": {
            "tag": "input"
        }, 
        "bind": {
            "type": "geotrace"
        }, 
        "hint": "GPS coordinates can only be collected when outside."
    }, 
    "end time": {
        "bind": {
            "jr:preload": "timestamp", 
            "type": "dateTime", 
            "jr:preloadParams": "end"
        }
    }, 
    "device id": {
        "bind": {
            "jr:preload": "property", 
            "type": "string", 
            "jr:preloadParams": "deviceid"
        }
    },
    "subscriberid": {
        "bind": {
            "jr:preload": "property", 
            "type": "string", 
            "jr:preloadParams": "subscriberid"
        }
    }, 
    "q barcode": {
        "control": {
            "tag": "input"
        }, 
        "bind": {
            "type": "barcode"
        }
    }, 
    "image": {
        "control": {
            "tag": "upload", 
            "mediatype": "image/*"
        }, 
        "bind": {
            "type": "binary"
        }
    }, 
    "q int": {
        "control": {
            "tag": "input"
        }, 
        "bind": {
            "type": "int"
        }
    }, 
    "add text prompt": {
        "control": {
            "tag": "input"
        }, 
        "bind": {
            "type": "string"
        }
    }, 
    "add date prompt": {
        "control": {
            "tag": "input"
        }, 
        "bind": {
            "type": "date"
        }
    }, 
    "q calculate": {
        "bind": {
            "type": "string"
        }
    }, 
    "start": {
        "bind": {
            "jr:preload": "timestamp", 
            "type": "dateTime", 
            "jr:preloadParams": "start"
        }
    }, 
    "trigger": {
        "control": {
            "tag": "trigger"
        }
    }, 
    "add acknowledge prompt": {
        "control": {
            "tag": "trigger"
        }, 
        "bind": {
            "type": "string"
        }
    }, 
    "percentage": {
        "control": {
            "tag": "input"
        }, 
        "bind": {
            "type": "int", 
            "constraint": "0 <= . and . <= 100"
        }
    }, 
    "get phone number": {
        "bind": {
            "jr:preload": "property", 
            "type": "string", 
            "jr:preloadParams": "phonenumber"
        }
    }, 
    "today": {
        "bind": {
            "jr:preload": "date", 
            "type": "date", 
            "jr:preloadParams": "today"
        }
    }, 
    "gps": {
        "control": {
            "tag": "input"
        }, 
        "bind": {
            "type": "geopoint"
        }, 
        "hint": "GPS coordinates can only be collected when outside."
    }, 
    "q date": {
        "control": {
            "tag": "input"
        }, 
        "bind": {
            "type": "date"
        }
    }, 
    "sim id": {
        "bind": {
            "jr:preload": "property", 
            "type": "string", 
            "jr:preloadParams": "simserial"
        }
    }, 
    "add decimal prompt": {
        "control": {
            "tag": "input"
        }, 
        "bind": {
            "type": "decimal"
        }
    }, 
    "number of days in last six months": {
        "control": {
            "tag": "input"
        }, 
        "bind": {
            "type": "int", 
            "constraint": "0 <= . and . <= 183"
        }, 
        "hint": "Enter a number 0-183."
    }, 
    "deviceid": {
        "bind": {
            "jr:preload": "property", 
            "type": "string", 
            "jr:preloadParams": "deviceid"
        }
    }, 
    "int": {
        "control": {
            "tag": "input"
        }, 
        "bind": {
            "type": "int"
        }
    }, 
    "add barcode prompt": {
        "control": {
            "tag": "input"
        }, 
        "bind": {
            "type": "barcode"
        }
    }, 
    "q decimal": {
        "control": {
            "tag": "input"
        }, 
        "bind": {
            "type": "decimal"
        }
    }, 
    "end": {
        "bind": {
            "jr:preload": "timestamp", 
            "type": "dateTime", 
            "jr:preloadParams": "end"
        }
    }, 
    "add calculate prompt": {
        "bind": {
            "type": "string"
        }
    }, 
    "add dateTime prompt": {
        "control": {
            "tag": "input"
        }, 
        "bind": {
            "type": "dateTime"
        }
    }, 
    "note": {
        "control": {
            "tag": "input"
        }, 
        "bind": {
            "readonly": "true()", 
            "type": "string"
        }
    }, 
    "add location prompt": {
        "control": {
            "tag": "input"
        }, 
        "bind": {
            "type": "geopoint"
        }
    }, 
    "get subscriber id": {
        "bind": {
            "jr:preload": "property", 
            "type": "string", 
            "jr:preloadParams": "subscriberid"
        }
    }, 
    "phone number": {
        "control": {
            "tag": "input"
        }, 
        "bind": {
            "type": "string", 
            "constraint": "regex(., '^\\d*$')"
        }, 
        "hint": "Enter numbers only."
    }, 
    "get device id": {
        "bind": {
            "jr:preload": "property", 
            "type": "string", 
            "jr:preloadParams": "deviceid"
        }
    }, 
    "add integer prompt": {
        "control": {
            "tag": "input"
        }, 
        "bind": {
            "type": "int"
        }
    }, 
    "q dateTime": {
        "control": {
            "tag": "input"
        }, 
        "bind": {
            "type": "dateTime"
        }
    }, 
    "date": {
        "control": {
            "tag": "input"
        }, 
        "bind": {
            "type": "date"
        }
    }, 
    "start time": {
        "bind": {
            "jr:preload": "timestamp", 
            "type": "dateTime", 
            "jr:preloadParams": "start"
        }
    }, 
    "number of days in last year": {
        "control": {
            "tag": "input"
        }, 
        "bind": {
            "type": "int", 
            "constraint": "0 <= . and . <= 365"
        }, 
        "hint": "Enter a number 0-365."
    }, 
    "date time": {
        "control": {
            "tag": "input"
        }, 
        "bind": {
            "type": "dateTime"
        }
    }, 
    "time": {
        "control": {
            "tag": "input"
        }, 
        "bind": {
            "type": "time"
        }
    }, 
    "audio": {
        "control": {
            "tag": "upload", 
            "mediatype": "audio/*"
        }, 
        "bind": {
            "type": "binary"
        }
    }, 
    "hidden": {
        "bind": {
            "type": "string"
        }
    },
    "uri:subscriberid": {
        "bind": {
            "jr:preload": "property", 
            "type": "string", 
            "jr:preloadParams": "uri:subscriberid"
        }
    },
    "uri:phonenumber": {
        "bind": {
            "jr:preload": "property", 
            "type": "string", 
            "jr:preloadParams": "uri:phonenumber"
        }
    },
    "uri:simserial": {
        "bind": {
            "jr:preload": "property", 
            "type": "string", 
            "jr:preloadParams": "uri:simserial"
        }
    },
    "uri:deviceid": {
        "bind": {
            "jr:preload": "property", 
            "type": "string", 
            "jr:preloadParams": "uri:deviceid"
        }
    }, 
    "username": {
        "bind": {
            "jr:preload": "property", 
            "type": "string", 
            "jr:preloadParams": "username"
        }
    }, 
    "uri:username": {
        "bind": {
            "jr:preload": "property", 
            "type": "string", 
            "jr:preloadParams": "uri:username"
        }
    }, 
    "email": {
        "bind": {
            "jr:preload": "property", 
            "type": "string", 
            "jr:preloadParams": "email"
        }
    },
    "uri:email": {
        "bind": {
            "jr:preload": "property",
            "type": "string", 
            "jr:preloadParams": "uri:email"
        }
    },
        "osm": {
            "control": {
                "tag": "upload",
                "mediatype": "osm/*"
            },
            "bind": {
                "type": "binary"
            }
        },
        "file": {
            "control": {
                "tag": "upload",
                "mediatype": FILE_MEDIA_TYPES
            },
            "bind": {
                "type": "binary"
            }
        },
        "add file prompt": {
            "control": {
                "tag": "upload",
                "mediatype": FILE_MEDIA_TYPES
            },
            "bind": {
                "type": "binary"
            }
        },
    
    # FIXME: These seemingly could be condensed to one entry per question type if 'pyxform.aliases.select' were put to use.
    # Select one.
    constants.SELECT_ONE:           _SELECT_1_TYPE_DICT,
    "add select one prompt using":  _SELECT_1_TYPE_DICT, # Already in 'pyxform.aliases.select'.
    "select one using":             _SELECT_1_TYPE_DICT,
    "q select1":                    _SELECT_1_TYPE_DICT,
    
    # Select multiple.
    constants.SELECT_ALL_THAT_APPLY:        _SELECT_TYPE_DICT, 
    "select all that apply":                _SELECT_TYPE_DICT, # Already in 'pyxform.aliases.select'.
    "select all that apply from":           _SELECT_TYPE_DICT, # Already in 'pyxform.aliases.select'.
    "add select multiple prompt using":     _SELECT_TYPE_DICT, # Already in 'pyxform.aliases.select'.
    "select multiple from":                 _SELECT_TYPE_DICT,
    "q select":                             _SELECT_TYPE_DICT,
    "select multiple using":                _SELECT_TYPE_DICT,
}
