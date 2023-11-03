#!/usr/bin/python3
def print_last_digit(dig):
    if dig >= 0:
        last_d = dig % 10
    else:
        last_d = dig % -10
        last_d *= -1

    print("{:d}".format(last_d), end='')
    return (last_d)
