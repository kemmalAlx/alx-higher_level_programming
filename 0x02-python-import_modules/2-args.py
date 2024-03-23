#!/usr/bin/python3

if __name__ == "__main__":
    """Program that prints the number of and the list of its arguments."""

import sys

len = len(sys.argv) - 1
if len == 0:
    print("0 arguments.")
else:
    if len == 1:
        print("{} argument:".format(len))
    else:
        print("{} arguments:".format(len))
    for i in range(1, len + 1):
        print("{}: {}".format(i, sys.argv[i]))
