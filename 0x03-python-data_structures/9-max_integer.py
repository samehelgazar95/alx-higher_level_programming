#!/usr/bin/python
def max_integer(my_list=[]):
    if not my_list:
        return None

    max = 0
    for ele in my_list:
        if ele > max:
            max = ele

    return max
