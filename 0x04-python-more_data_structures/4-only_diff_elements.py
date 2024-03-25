#!/usr/bin/python3
# my code
def My_only_diff_elements(set_1, set_2):
    new_set = []
    for s in set_1:
        if s not in set_2:
            new_set.append(s)
    for s in set_2:
        if s not in set_1:
            new_set.append(s)
    return new_set

# simplifier code by Copilot
def only_diff_elements(set_1, set_2):
    return set_1 ^ set_2
