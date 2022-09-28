#!/usr/bin/python3
"""
a class Student
"""


class Student:
    """
    Definition of the Student class
    """
    def __init__(self, first_name, last_name, age):
        """
        Instantiation of the class with:
        first_name
        last_name
        age
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        retrieves a dictionary representation
        of a Student instance
        """
        class_dict = self.__dict__
        return class_dict
