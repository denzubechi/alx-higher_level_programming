#!/usr/bin/python3
"""
Class inheritance
"""


class MyList(list):
    """
    a class MyList that inherits from list
    """

    def print_sorted(self):
        """
        prints the sorted list
        """
        print(sorted(self))
