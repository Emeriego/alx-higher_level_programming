#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    kList = list(a_dictionary.keys())
    for item in kList:
        if value == a_dictionary.get(item):
            del a_dictionary[item]
    return (a_dictionary)
