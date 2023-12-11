#!/usr/bin/python3
import models.base
import models.rectangle
import models.square

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


if __name__ == "__main__":

    r1 = Rectangle(10, 2)
    print(r1.id)

    r2 = Rectangle(2, 10)
    print(r2.id)

    r3 = Rectangle(10, 2, 0, 0, 12)
    print(r3.id)
    
    
    print(Base.__doc__)
    print(models.base.__doc__)
    print("----------")
    print(Rectangle.__doc__)
    print(models.rectangle.__doc__)
    print("----------")
    print(Square.__doc__)
    print(models.square.__doc__)
    