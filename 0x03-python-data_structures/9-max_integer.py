#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) < 1:
        return None

    max = 0
    for ele in my_list:
        if ele >= max:
            max = ele

    return max
