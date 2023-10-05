#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys

argv = sys.argv
length = len(argv)

if __name__ == "__main__":
    if length < 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    n1 = int(argv[1])
    operator = argv[2]
    n2 = int(argv[3])
    if operator == "+":
        print("{} + {} = {}".format(n1, n2, add(n1, n2)))
    elif operator == "-":
        print("{} - {} = {}".format(n1, n2, sub(n1, n2)))
    elif operator == "*":
        print("{} * {} = {}".format(n1, n2, mul(n1, n2)))
    elif operator == "/":
        print("{} / {} = {}".format(n1, n2, div(n1, n2)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
