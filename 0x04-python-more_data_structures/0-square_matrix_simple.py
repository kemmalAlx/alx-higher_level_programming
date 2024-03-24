#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_2Dmatrix = []
    for row in matrix:
        new_matrix = []
        for column in row:
            new_matrix.append(column * column)
        new_2Dmatrix.append(new_matrix)
    return new_2Dmatrix
