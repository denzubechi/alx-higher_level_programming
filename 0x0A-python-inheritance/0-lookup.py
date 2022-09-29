#!/usr/bin/python3
"""
class module
"""


def lookup(obj):
    """
    a function that returns the list
    of available attributes and methods
    of an object

    return: a list
    """
    return dir(obj)
