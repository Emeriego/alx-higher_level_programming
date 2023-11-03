#!/usr/bin/python3
def remove_char_at(str, n):
    count = 0
    new_str = ""
    for ch in str:
        if count != n:
            new_str += ch
        count += 1
    return new_str
