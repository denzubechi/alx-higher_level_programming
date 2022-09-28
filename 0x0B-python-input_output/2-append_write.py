#!/usr/bin/python3
"""
a function that appendsat the end of a
text file (UTF8) and returns the number
of characters added
"""


def append_write(filename="", text=""):
    """
    appending characters function
    """
    with open(filename, 'a', encoding="utf-8") as f:
        write_txt = f.write(text)
        return write_txt
