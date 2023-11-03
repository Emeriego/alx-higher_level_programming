#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    arg_len = len(sys.argv) - 1
    if arg_len != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    my_opr = sys.argv[2]
    if my_opr != '+' and my_opr != '-' and my_opr != '*' and my_opr != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    from calculator_1 import add, sub, mul, div
    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if my_opr == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif my_opr == '-':
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif my_opr == '*':
        print("{} * {} = {}".format(a, b, mul(a, b)))
    else:
        print("{} / {} = {}".format(a, b, div(a, b)))
