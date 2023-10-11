#!/usr/bin/python3

def weight_average(my_list=[]):
    result = 0
    if len(my_list) == 0:
        return result
    div = 0
    for i in my_list:
        result += i[0] * i[1]
    for i in my_list:
        div += i[1]
    return (result / div)
