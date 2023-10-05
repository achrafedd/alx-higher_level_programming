#!/usr/bin/python3
import sys

length = len(sys.argv)

if __name__ == "__main__":
    i = 1
    if length < 2:
        print("0 arguments.")
    else:
        if length == 2:
            print("{} argument:".format(length - 1))
        else:
            print("{} arguments:".format(length - 1))
        while i < length:
            print("{}: {}".format(i, sys.argv[i]))
            i += 1
