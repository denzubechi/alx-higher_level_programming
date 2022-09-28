#!/usr/bin/python3

"""
 a function that returns the JSON
 representation of an object (string)
"""


import json


def to_json_string(my_obj):
    """
    JSON representation of an object
    """
    return json.dumps(my_obj)
