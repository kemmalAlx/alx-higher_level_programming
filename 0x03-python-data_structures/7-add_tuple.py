#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_a = len(tuple_a)
    len_b = len(tuple_b)
    if len_a == 0:
        tuple_a = 0, 0
    if len_a == 1:
        tuple_a = tuple_a[0], 0
    if len_b == 0:
        tuple_b = 0, 0
    if len_b == 1:
        tuple_b = tuple_b[0], 0
    return tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]


tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, (1, )))
print(add_tuple(tuple_a, ()))

""" 
To do
if t_a < 2
    use 0 for each messing
if t_b < 2
    use 0 for each messing
    
"""