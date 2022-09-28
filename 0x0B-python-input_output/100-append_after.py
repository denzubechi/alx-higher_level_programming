#!/usr/bin/python3
"""
a function that inserts a line of text to a file,
after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """
    insert function
    """
    text_file = ""
    with open(filename) as f:
        for line in f:
            text_file += line
            if search_string in line:
                text_file += new_string
    with open(filename, "w") as f:
        f.write(text_file)
