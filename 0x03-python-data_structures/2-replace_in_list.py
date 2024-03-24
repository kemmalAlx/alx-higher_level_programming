#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    count = len(my_list)
    if idx < 0 or idx >= count:
        return None
    new_list = []
    for list in my_list:
        new_list.append(list)
    new_list[idx] = element
    return new_list
