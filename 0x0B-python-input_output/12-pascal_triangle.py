#!/usr/bin/python3
""" Pascal Triangle Module
"""

# n = 5
# [[1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1]]

def pascal_triangle(n):
    """ Pascal Triangle Func
    """
    
    pascal = []
    
    if (n <= 0):
        return pascal
    
    for i in range(n):
        pascal.append([1 * (i + 1)])
        
    print(pascal)
    

    
pascal_triangle(5)
