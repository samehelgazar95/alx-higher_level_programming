#!/usr/bin/python3
""" 2-matrix_divided module """


def matrix_divided(matrix, div):
    """ matrix_divided function

        Args:
            matrix: the 2d matrix
            div: the denominator

        Raises:
            TypeError: if elements of the matrix is not int or float
                        if len of rows is not equal
                        if div is not a number
            ZeroDivisionError: if div equals Zero
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if any(type(e) not in (int, float) for r in matrix for e in r):
        raise TypeError(msg)

    row_len_set = {len(row) for row in matrix}
    if len(row_len_set) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    res = [[0] * len(matrix[0]) for _ in range(len(matrix))]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            res[i][j] = round(matrix[i][j] / div, 2)

    return res


if __name__ == '__main__':
    import doctest
    doctest.testfile("./tests/2-matrix_divided.txt")
