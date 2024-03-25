#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for list in my_list:
        if (list == search):
            new_list.append(replace)
        else:
            new_list.append(list)
    return new_list
