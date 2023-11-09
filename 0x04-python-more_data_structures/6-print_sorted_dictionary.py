#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_dict = {k: a_dictionary[k] for k in sorted(a_dictionary)}

    for key, val in new_dict.items():
        print("{}: {}".format(key, val))
