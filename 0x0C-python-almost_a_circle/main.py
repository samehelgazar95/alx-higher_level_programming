#!/usr/bin/python3
""" 15-main """
from models.square import Square

if __name__ == "__main__":

    r1 = Square(1)
    Square.save_to_file([r1])

    with open("Square.json", "r") as file:
        print(file.read())
