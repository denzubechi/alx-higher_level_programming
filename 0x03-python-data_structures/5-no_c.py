#!/usr/bin/python3
def no_c(my_string):
    strings = ""
    for i in my_string:
        if i == "c" or i =="C":
            continue
        else:
            strings += i
    return strings
