#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = len(sys.argv) - 1

    if i == 1:
        print("{} argument.".format(i))
    else:
        print("{} arguments:".format(i))

    if i >= 1:
        i = 0
        for items in sys.argv:
            if i != 0:
                print("{}: {}".format(i, items))
            i += 1