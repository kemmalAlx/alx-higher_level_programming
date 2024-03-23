#!/usr/bin/python3

for c in reversed(range(ord('a'), ord('z') + 1)):
    char = c if c % 2 == 0 else c - 32
    print("{}".format(chr(char)), end="")
