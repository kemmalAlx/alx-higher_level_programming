#!/usr/bin/python3

if __name__ == "__main__":
    """100-my_calculator.py"""

    from calculator_1 import add, sub, mul, div
    from sys import argv


    if len(argv) - 1 != 3:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    op = argv[2]
    if op == '+':
        print("{} {} {} = {}".format(a, op, b, add(a, b)))
    if op == '*':
        print("{} {} {} = {}".format(a, op, b, mul(a, b)))
    if op == '-':
        print("{} {} {} = {}".format(a, op, b, sub(a, b)))
    if op == '/':
        print("{} {} {} = {}".format(a, op, b, div(a, b)))
