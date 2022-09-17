#!/usr/bin/python3
"""
a module Sqaure that defines a square
"""


class Square:
    """
    Definition of a Class Square:
    Private instance attribute: size
    Instantiation with size (no type/value verification)
    You are not allowed to import any module
    """
    def __init__(self, size):
        """
        initializes the square
        """
        self.__size = size
