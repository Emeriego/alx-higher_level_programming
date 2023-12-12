#!/usr/bin/python3
"""Module creates Pascal's Triangle function."""


def pascal_triangle(n):
    """func represents Pascal's Triangle of size n.
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        angl = triangles[-1]
        tmp = [1]
        for idx in range(len(angl) - 1):
            tmp.append(angl[idx] + angl[idx + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
