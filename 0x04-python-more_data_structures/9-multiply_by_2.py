#!/usr/bin/python3
# my code
def My_multiply_by_2(a_dictionary):
    new_dict = {}
    for key, value in a_dictionary.items():
        new_dict[key] = value * 2
    return new_dict

# simplified code from copilot
def multiply_by_2(a_dictionary):
    return {key: val * 2 for key, val in a_dictionary.items()}
