#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    new = {key: value}
    newDir = a_dictionary.update(new)
    return newDir
