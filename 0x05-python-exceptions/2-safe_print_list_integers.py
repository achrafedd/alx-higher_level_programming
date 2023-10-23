#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    length = 0
    i = 0
    while x > 0:
        try:
            print("{:d}".format(my_list[i]), end="")
            i += 1
            x -= 1
        except (ValueError, TypeError):
            i += 1
            x -= 1
            continue
        length += 1
    print()
    return length
