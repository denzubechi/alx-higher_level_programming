#!/usr/bin/python3
"""
a function that defines pascal's triangle
"""


def pascal_triangle(n):
    """
    Pascal's triangle fucntion:
        Returns an empty list if n <= 0
    """
    if n <= 0:
        return []

    pascals_tri = []

    for i in range(n):
        pascals_tri.append([1]*(i+1))

    for i in range(2, n):
        for j in range(1, i):
            pascals_tri[i][j] = pascals_tri[i-1][j-1] + pascals_tri[i-1][j]

    return pascals_tri
