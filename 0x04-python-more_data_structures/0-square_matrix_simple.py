#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_list = []

    for l in matrix:
        arr = []

        for num in l:
            arr.append(num ** 2)
        new_list.append(arr)
    return new_list
