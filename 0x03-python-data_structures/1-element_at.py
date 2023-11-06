#!/usr/bin/python3
def element_at(my_list, idx):
    if idx > (len(my_list) - 1) or idx < 0:
        print("None")
    else:
        print("{}".format(my_list[idx]))
