#!/usr/bin/python3
"""
a class MyInt that inherits from int
"""


class MyInt(int):
    """
    MyInt is a rebel.
    MyInt has == and != operators inverted
    """
    def __eq__(self, other):
        """
        rebel class (!=)
        """
        return self.real != other

    def __ne__(self, other):
        """
        rebel class (==)
        """
        return self.real == other
