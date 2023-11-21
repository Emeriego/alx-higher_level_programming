#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    res = []
    curr = 0
    for item in range(0, list_length):
        try:
            curr = my_list_1[item] / my_list_2[item]

        except TypeError:
            curr = 0
            print("wrong type")

        except ZeroDivisionError:
            curr = 0
            print("division by 0")

        except IndexError:
            curr = 0
            print("out of range")
        finally:
            pass
        res.append(curr)

    return res
