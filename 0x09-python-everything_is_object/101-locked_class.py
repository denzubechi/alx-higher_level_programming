#!/usr/bin/python3

"""Defines a locked class."""


class LockedClass:
    """
    prevents the user from dynamically
    creating new instances
    """
    __slots__ = ["first_name"]
