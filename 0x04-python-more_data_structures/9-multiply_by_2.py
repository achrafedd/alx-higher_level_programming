#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    return dict(map(lambda x: (x, a_dictionary[x] * 2), a_dictionary))
