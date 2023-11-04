#!/usr/bin/python

def element_at(my_list, idx):
    if not idx:
        return None

    for i in range(0, len(my_list) - 1):
        if i == idx:
            return my_list[i]
    else:
        return None
