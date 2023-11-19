#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    score_key = None
    score_val = 0

    for key in a_dictionary.keys():
        if a_dictionary[key] > score_val:
            score_val = a_dictionary[key]
            score_key = key

    return score_key
