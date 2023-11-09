#!/usr/bin/python3
def to_subtract(nList):
    to_sub = 0
    ml = max(nList)

    for item in nList:
        if ml > item:
            to_sub += item

    return (ml - to_sub)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    ro_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_keys = list(ro_num.keys())

    n = 0
    nList = [0]
    last_rom = 0
    for ch_str in roman_string:
        for r_num in list_keys:
            if r_num == ch_str:
                if ro_num.get(ch_str) <= last_rom:
                    n += to_subtract(nList)
                    nList = [ro_num.get(ch_str)]
                else:
                    nList.append(ro_num.get(ch_str))
                last_rom = ro_num.get(ch_str)
    n += to_subtract(nList)
    return (n)
