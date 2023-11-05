#!/usr/bin/python3
def no_c(my_string):
    res = ''.join(char for char in my_string if char not in 'cC')
    return res
