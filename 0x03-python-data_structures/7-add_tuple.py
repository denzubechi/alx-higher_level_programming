#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 1:
        tuple_0 = tuple_a[0] + tuple_b[0]
        tuple_1 = 0 + tuple_b[1]
    elif len(tuple_b) == 1:
        tuple_0 = tuple_a[0] + tuple_b[0]
        tuple_1 = tuple_a[1] + 0
    elif len(tuple_a) and len(tuple_b) > 1:
        tuple_0 = tuple_a[0] + tuple_b[0]
        tuple_1 = tuple_a[1] + tuple_b[1]
    elif len(tuple_a) == 0:
        tuple_0 = 0 + tuple_b[0]
        tuple_1 = 0 + tuple_b[1]
    elif len(tuple_b) == 0:
        tuple_0 = tuple_a[0] + 0
        tuple_1 = tuple_a[1] + 0
    return tuple_0, tuple_1
