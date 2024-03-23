#!/usr/bin/python3

def remove_char_at(str, n):
    newStr = ""
    for i in range(0, len(str)):
        if (i != n):
            newStr += str[i]
        i += 1
    return newStr
