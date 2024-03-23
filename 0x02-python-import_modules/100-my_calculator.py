#!/usr/bin/python3

if __name__ == "__main__":
    """100-my_calculator.py"""

    from calculator_1 import add, sub, mul, div
    from sys import argv


    len = len(argv) -1
    if len != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    op = argv[2]
    b = int(argv[3])
    list = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': div
    }
    if op in list.keys():
        print("{} {} {} = {}".format(a, op, b, list[op](a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
