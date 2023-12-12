#!/usr/bin/python3
""" 17-main """
from models.square import Square

if __name__ == "__main__":

    r1 = Square(3, 5, 1)
    r1.update(2)

    print(Square.__dict__)