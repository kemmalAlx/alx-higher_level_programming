#!/usr/bin/python3
for nbr in range(100):
    if nbr < 10:
        print('0{}'.format(nbr), end="")
    else:
        print("{}".format(nbr), end="")
    if nbr != 99:
        print(", ", end="")
    else:
        print(end="\n")
