#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for my_list in matrix:
        i = 0
        for item in my_list:
            print("{:d}".format(item), end=" " if i != (len(my_list) - 1) else "")
            i += 1
        print("")
