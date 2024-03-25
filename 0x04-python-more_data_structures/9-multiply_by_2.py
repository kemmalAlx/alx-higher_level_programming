#!/usr/bin/python3
# my code
# def My_multiply_by_2(a_dictionary):
#     new_dict = {}
#     for key in a_dictionary:
#         new_dict[key] = a_dictionary[key] * 2
#     return new_dict

# simplified code from copilot
def multiply_by_2(a_dictionary):
    return {key: val * 2 for key, val in a_dictionary.items()}

def test():
    val = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}
    for key, value in val.items():
        print("key: {}, val: {}".format(key, value))

test()