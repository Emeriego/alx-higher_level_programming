#!/usr/bin/python3
def no_c(my_string):
    i = 0
    for ch in my_string:
        if ch == 'c' or ch == 'C':
            del my_string[i]
        i = i + 1
