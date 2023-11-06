#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for my_list in matrix:
        for item in my_list:
            print("{:d}".format(item), end=" ")
        print("\n", end="")
