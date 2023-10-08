#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for l in matrix:
        for n in l:
            print("{:d}".format(n), end=" ")
        print("")
