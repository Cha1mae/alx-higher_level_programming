#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    for d in range(len(matrix)):
        new_matrix[d] = list(map(lambda c: c**2, matrix[d]))
    return (new_matrix)
