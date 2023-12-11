#!/usr/bin/python3
from models.base import Base
import models.base
from models.rectangle import Rectangle
import models.rectangle
from models.square import Square
import models.square

if __name__ == '__main__':
    b = Base()
    print(b.__doc__)
    print(models.base.__doc__)
    
    r = Rectangle(1, 1)
    print(r.__doc__)
    print(models.rectangle.__doc__)
        
    s = Square(1, 1)
    print(s.__doc__)
    print(models.square.__doc__)
    