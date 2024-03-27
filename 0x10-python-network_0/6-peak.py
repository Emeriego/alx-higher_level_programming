#!/usr/bin/python3
""" Finds a peak"""

def find_peak(list_of_integers):
    """
    list_of_integers(int): list of integers to find peak of returns
    eak of list_of_integers or None
    """
    size = len(list_of_integers)
    midle = size
    mid = size // 2

    if size == 0:
        return None

    while True:
        midle = midle // 2
        if (mid < size - 1 and
                list_of_integers[mid] < list_of_integers[mid + 1]):
            if midle // 2 == 0:
                midle = 2
            mid = mid + midle // 2
        elif midle > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
            if midle // 2 == 0:
                midle = 2
            mid = mid - midle // 2
        else:
            return list_of_integers[mid]
