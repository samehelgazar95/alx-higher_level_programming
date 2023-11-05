#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return None

    res_list = []
    for i in range(len(my_list)):
        res_list.append(True if (my_list[i] % 2 == 0) else False)

    return res_list
