#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return

    for row in matrix:
        for ele in row:
            print("{}".format(ele), end=' ')
        print()
