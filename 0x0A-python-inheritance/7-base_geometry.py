#!/usr/bin/python3

"""
Defines an empty class BaseGeometry.
"""


class BaseGeometry:
    """
    Represent base geometry.
    """

    def area(self):
        """Raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates an integer value:
        Args:
            name (str): name of the parameter to validate
            value (int): parameter to validate
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is <= 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
