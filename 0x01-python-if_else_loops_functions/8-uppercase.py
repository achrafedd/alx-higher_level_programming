#!/usr/bin/python3

def uppercase(str):
    for c in str:
        is_lower = ord(c) >= 97 and ord(c) <= 122
        print("{:c}".format(ord(c) - 32 if is_lower else ord(c)), end="")
    print("")
