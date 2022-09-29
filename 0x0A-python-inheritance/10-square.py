#!/usr/bin/python3
"""
a ssuare class that inherits from rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    a square class deifinition
    """

    def __init__(self, size):
        """
        Initializing the class
        Args:
            size (int): The size of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
