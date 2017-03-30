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

_IMAGE_TYPE= {
    "control": {
        "tag": "upload",
        "mediatype": "image/*"
    }, 
    "bind": {
        "type": "binary"
    }
}

_VIDEO_TYPE= {
    "control": {
        "tag": "upload", 
        "mediatype": "video/*"
    }, 
    "bind": {
        "type": "binary"
    }
}

_AUDIO_TYPE= {
    "control": {
        "tag": "upload", 
        "mediatype": "audio/*"
    }, 
    "bind": {
        "type": "binary"
    }
}

_DATE_TYPE= {
    "control": {
        "tag": "input"
    }, 
    "bind": {
        "type": "date"
    }
}

_DATETIME_TYPE= {
    "control": {
        "tag": "input"
    }, 
    "bind": {
        "type": "dateTime"
    }
}

_GEOPOINT_TYPE= {
    "control": {
        "tag": "input"
    }, 
    "bind": {
        "type": "geopoint"
    }
}

_GEOPOINT_TYPE_W_HINT= dict(_GEOPOINT_TYPE, \
    **{"hint": "GPS coordinates can only be collected when outside."})

_GEOSHAPE_TYPE= {
    "control": {
        "tag": "input"
    }, 
    "bind": {
        "type": "geoshape"
    }
}

_GEOSHAPE_TYPE_W_HINT= dict(_GEOSHAPE_TYPE, \
            **{"hint": "GPS coordinates can only be collected when outside."})

_GEOTRACE_TYPE= {
    "control": {
        "tag": "input"
    }, 
    "bind": {
        "type": "geotrace"
    }
}

_GEOTRACE_TYPE_W_HINT= dict(_GEOTRACE_TYPE, \
            **{"hint": "GPS coordinates can only be collected when outside."})

_INT_TYPE= {
    "control": {
        "tag": "input"
    }, 
    "bind": {
        "type": "int"
    }
}

_DECIMAL_TYPE= {
    "control": {
        "tag": "input"
    }, 
    "bind": {
        "type": "decimal"
    }
}

_STRING_TYPE= {
    "control": {
        "tag": "input"
    }, 
    "bind": {
        "type": "string"
    }
}

_NOTE_TYPE= {
    "control": {
        "tag": "input"
    }, 
    "bind": {
        "readonly": "true()", 
        "type": "string"
    }
}

_TRIGGER_TYPE= {
    "control": {
        "tag": "trigger"
    }, 
    "bind": {
        "type": "string"
    }
}

_BARCODE_TYPE= {
    "control": {
        "tag": "input"
    }, 
    "bind": {
        "type": "barcode"
    }
}

_PHONENUMBER_TYPE= {
    "bind": {
        "jr:preload": "property", 
        "type": "string", 
        "jr:preloadParams": "phonenumber"
    }
}

_START_TYPE= {
    "bind": {
        "jr:preload": "timestamp", 
        "type": "dateTime", 
        "jr:preloadParams": "start"
    }
}

_END_TYPE= {
    "bind": {
        "jr:preload": "timestamp", 
        "type": "dateTime", 
        "jr:preloadParams": "end"
    }
}

_SIMSERIAL_TYPE= {
    "bind": {
        "jr:preload": "property", 
        "type": "string", 
        "jr:preloadParams": "simserial"
    }
}

_DEVICEID_TYPE= {
    "bind": {
        "jr:preload": "property", 
        "type": "string", 
        "jr:preloadParams": "deviceid"
    }
}

_SUBSCRIBERID_TYPE= {
    "bind": {
        "jr:preload": "property", 
        "type": "string", 
        "jr:preloadParams": "subscriberid"
    }
}

_TODAY_TYPE= {
    "bind": {
        "jr:preload": "date", 
        "type": "date", 
        "jr:preloadParams": "today"
    }
}

_NONINPUT_STING_TYPE= {
    "bind": {
        "type": "string"
    }
}

QUESTION_TYPE_DICT = \
{
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
    
    "q picture":            _IMAGE_TYPE,
    "photo":                _IMAGE_TYPE,
    "q image":              _IMAGE_TYPE,
    "add image prompt":     _IMAGE_TYPE,
    "image":                _IMAGE_TYPE,
    
    "add date time prompt":     _DATETIME_TYPE,
    "q date time":              _DATETIME_TYPE,
    
    "video":                _VIDEO_TYPE,
    "add video prompt":     _VIDEO_TYPE,
    "q video":              _VIDEO_TYPE,
    
    "add audio prompt":     _AUDIO_TYPE,
    "q audio":              _AUDIO_TYPE,
    "audio":                _AUDIO_TYPE,
    
    "add date prompt":  _DATE_TYPE,
    "q date":           _DATE_TYPE,
    "date":             _DATE_TYPE,
    
    "datetime":             _DATETIME_TYPE, 
    "dateTime":             _DATETIME_TYPE, 
    "add dateTime prompt":  _DATETIME_TYPE, 
    "q dateTime":           _DATETIME_TYPE, 
    "date time":            _DATETIME_TYPE, 
    
    "q geopoint":           _GEOPOINT_TYPE,
    "location":             _GEOPOINT_TYPE,
    "q location":           _GEOPOINT_TYPE,
    "add location prompt":  _GEOPOINT_TYPE,
    
    "geopoint":     _GEOPOINT_TYPE_W_HINT,
    "gps":          _GEOPOINT_TYPE_W_HINT,
    
    "q geotrace":   _GEOTRACE_TYPE,
    
    "geotrace":     _GEOTRACE_TYPE_W_HINT,
    
    "q geoshape":   _GEOSHAPE_TYPE,
    
    "geoshape":     _GEOSHAPE_TYPE_W_HINT,

    "integer":              _INT_TYPE,
    "q int":                _INT_TYPE,
    "int":                  _INT_TYPE,
    "add integer prompt":   _INT_TYPE,
    
    "decimal":              _DECIMAL_TYPE,
    "add decimal prompt":   _DECIMAL_TYPE,
    "q decimal":            _DECIMAL_TYPE,
    
    "text":                 _STRING_TYPE,
    "string":               _STRING_TYPE,
    "q string":             _STRING_TYPE,
    "select one external":  _STRING_TYPE,
    "add text prompt":      _STRING_TYPE,
    
    "add note prompt":  _NOTE_TYPE,
    "q note":           _NOTE_TYPE,
    "note":             _NOTE_TYPE,

    "add acknowledge prompt":   _TRIGGER_TYPE,
    "acknowledge":              _TRIGGER_TYPE,
    "q acknowledge":            _TRIGGER_TYPE,
    
    "add barcode prompt":   _BARCODE_TYPE,
    "q barcode":            _BARCODE_TYPE,
    "barcode":              _BARCODE_TYPE,

    "phonenumber":          _PHONENUMBER_TYPE,
    "get phone number":     _PHONENUMBER_TYPE,
    
    "start":            _START_TYPE,
    "get start time":   _START_TYPE,
    
    "get end time":     _END_TYPE,
    "end time":         _END_TYPE,
    "end":              _END_TYPE,
    
    "get sim id":   _SIMSERIAL_TYPE,
    "simserial":    _SIMSERIAL_TYPE,
    "sim id":       _SIMSERIAL_TYPE,
    
    "imei":             _DEVICEID_TYPE,
    "device id":        _DEVICEID_TYPE,
    "get device id":    _DEVICEID_TYPE,
    "deviceid":         _DEVICEID_TYPE,

    "subscriber id":        _SUBSCRIBERID_TYPE,
    "subscriberid":         _SUBSCRIBERID_TYPE,
    "get subscriber id":    _SUBSCRIBERID_TYPE,
    
    "get today":            _TODAY_TYPE,
    "today":                _TODAY_TYPE,
    
    "start time":   _START_TYPE,
    
    "calculate":                _NONINPUT_STING_TYPE,
    "q calculate":              _NONINPUT_STING_TYPE,
    "add calculate prompt":     _NONINPUT_STING_TYPE, 
    "hidden":                   _NONINPUT_STING_TYPE,
    
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
    "trigger": {
        "control": {
            "tag": "trigger"
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
    "time": {
        "control": {
            "tag": "input"
        }, 
        "bind": {
            "type": "time"
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
