#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            new = chr(ord(c) - 32)
        else:
            new = c
        print("{}".format(new), end="")
    print("")
