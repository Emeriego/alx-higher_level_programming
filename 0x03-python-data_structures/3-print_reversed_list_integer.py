#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if isinstance(my_list, list):
        rev_list = my_list.reverse()
        for item in rev_list:
            print("{:d}".format(item))
