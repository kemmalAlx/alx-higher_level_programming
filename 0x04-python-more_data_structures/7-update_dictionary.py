#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    new = {key: value}
    newDir = a_dictionary.update(new)
    return newDir

# print_sorted_dictionary = __import__('6-print_sorted_dictionary').print_sorted_dictionary


# a_dictionary = { 'a': "a", 'b': "b" , 'c': "c", 'd': "d", 'e': "e" } 
# key = "a" 
# value = "A"



# new_dict = update_dictionary(a_dictionary, key, value)
# print_sorted_dictionary(new_dict)
# print("--")
# print_sorted_dictionary(a_dictionary)