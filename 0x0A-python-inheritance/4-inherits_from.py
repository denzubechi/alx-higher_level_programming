#!/usr/bin/python3
"""
Definining a function that checks for
direct or indirect inheritance
"""


def inherits_from(obj, a_class):
    """
    a function that returns True if the object
    is an instance of a class that inherited (directly or indirectly)
    from the specified class; otherwise False
    """
    if issubclass(type(obj), a_class) and (type(obj) is not a_class):
        return True
    return False
