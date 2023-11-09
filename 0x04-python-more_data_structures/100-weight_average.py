#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    c = 0
    my_num = 0
    for item in my_list:
        my_num = my_num + (item[0] * item[1])
        c = c + item[1]
    return (my_num / c)
