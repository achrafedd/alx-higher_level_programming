#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except ValueError as err:
        sys.stderr.write("Exception: {}\n".format(err.args[0]))
        return False
    except TypeError as err:
        sys.stderr.write("Exception: {}\n".format(err.args[0]))
        return False
    return True
