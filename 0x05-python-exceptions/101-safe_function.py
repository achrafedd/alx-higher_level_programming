#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    result = None
    try:
        result = fct(args[0], args[1])
    except Exception as err:
        result = None
        sys.stderr.write("Exception: {}\n".format(err.args[0]))
    return result
