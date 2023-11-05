#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list

    first = my_list[0:idx]
    second = my_list[idx + 1:len(my_list)]
    my_list = first + second

    return my_list
