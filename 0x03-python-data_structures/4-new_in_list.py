#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = []
    new_list.extend(my_list)
    list_range = len(my_list)
    if idx < 0:
        return my_list
    elif idx > list_range:
        return my_list
    else:
        new_list[idx] = element
        return new_list
