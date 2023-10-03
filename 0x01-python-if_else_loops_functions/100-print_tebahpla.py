#!/usr/bin/python3

assci = 122

while assci >= 97:
    is_even = assci % 2 == 0
    print("{:c}".format(assci if is_even else (assci - 32)), end="")
    assci -= 1
