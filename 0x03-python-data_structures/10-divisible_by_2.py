#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return None
    result = []
    for list in my_list:
        result.append(True) if list % 2 == 0 else result.append(False)
    return result
