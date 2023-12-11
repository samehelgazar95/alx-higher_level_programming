#!/usr/bin/python3
""" 15-main """
from models.rectangle import Rectangle
from models.square import Square

if __name__ == "__main__":

    # r1 = Square()
    r2 = Rectangle(2, 4)
    Rectangle.save_to_file([r2])

    with open("Rectangle.json", "r") as file:
        print(file.read())
