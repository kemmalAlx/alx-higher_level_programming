#!/usr/bin/python3
def safe_print_list(my_list = [], x = 0):
    try:
        len = 0
        for i, list in enumerate(my_list):
            if i < x:
                len+=1
                print(list, end="")
        print()
        return len
    except:
        return
