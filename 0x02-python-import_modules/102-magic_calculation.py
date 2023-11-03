#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_102_helper import add, sub
    if a < b:
        res = add(a, b)
        for k in range(4, 6):
            res = add(res, k)
        return (res)
    else:
        return (sub(a, b))
