#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None

    for row in matrix:
        if (len(row) == 0):
            print()
        for ele in row:
            print("{:d}".format(ele),
                  end='\n' if ele == row[len(row) - 1] else ' ')
