#!/usr/bin/python3

"""
a function that writes an Object
to a text file, using a JSON
representation
"""


import json


def save_to_json_file(my_obj, filename):
    """
    JSON representation of writing an object
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
