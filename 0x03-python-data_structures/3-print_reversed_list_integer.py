#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    id = len(my_list) - 1
    
    while id >= 0:
        print("{:d}".format(my_list[id]))
        id -= 1
