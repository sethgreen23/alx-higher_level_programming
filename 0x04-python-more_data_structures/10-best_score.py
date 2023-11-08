#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return (None)
    max_score = 0
    max_score_owner = ""
    for key, value in a_dictionary.items():
        if a_dictionary[key] > max_score:
            max_score = a_dictionary[key]
            max_score_owner = key
    return (max_score_owner)
