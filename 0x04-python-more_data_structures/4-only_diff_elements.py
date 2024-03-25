#!/usr/bin/python3

# my code
def My_only_diff_elements(set_1, set_2):
    new_set = []
    for s in set_1:
        new_set.append(s)
    for s in set_2:
        new_set.append(s)
    my_dict = {i : new_set. count(i) for i in new_set}
    ret = []
    for m in my_dict:
        if my_dict[m] == 1:
            ret.append(m)
    return ret

# simplifier code by Copilot
def only_diff_elements(set_1, set_2):
    return set_1 ^ set_2
