#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    length = 0
    while x > 0:
        try:
            print("{}".format(my_list[length]), end="")
        except IndexError:
            print()
            return length
        x -= 1
        length += 1
    print()
    return length
