#!/usr/bin/python3

def remove_char_at(str, n):
    if len(str) < n and n < 0:
        return str
    chars = range(0, len(str))
    new_str = ""
    for i in chars:
        if i == n:
            continue
        new_str += str[i]
    return new_str
