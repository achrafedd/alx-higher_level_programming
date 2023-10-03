#!/usr/bin/python3

assci = range(97, 123)

for i in assci:
    if i == 101 or i == 113:
        continue
    print("{:c}".format(i), end="")
