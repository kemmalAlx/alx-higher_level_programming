#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if not a_dictionary:
        return
    sort = sorted(a_dictionary.items())
    for key, value in sort:
        print("{}: {}".format(key, value))
