#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    best_score = 0
    best_key = None
    for key, score in a_dictionary.items():
        if score > best_score:
            best_key = key
            best_score = score
    return best_key
