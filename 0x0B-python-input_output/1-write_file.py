#!/usr/bin/python3
"""
a function that writes a string to a
text file (UTF8) and returns the number
of characters
"""


def write_file(filename="", text=""):
    """
    write_file function
    """
    with open(filename, 'w', encoding="utf-8") as f:
        write_txt = f.write(text)
        return write_txt
