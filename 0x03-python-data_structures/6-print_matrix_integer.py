#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        count = len(i)
        cp = 0
        for j in i:
            cp += 1
            if cp == count:
                print("{}".format(j))
            else:
                print("{}".format(j), end=" ")
