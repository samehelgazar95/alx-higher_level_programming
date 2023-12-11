#!/usr/bin/python3
import models.base
import models.rectangle
import models.square

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


if __name__ == "__main__":
    
    r1 = Rectangle(10, 7, 2, 8)
    dictionary = r1.to_dictionary()
    json_dictionary = Base.to_json_string([dictionary])
    print(dictionary)
    print(type(dictionary))
    print(json_dictionary)
    print(type(json_dictionary))
    
    print(Base.__doc__)
    print(models.base.__doc__)
    print("----------")
    print(Rectangle.__doc__)
    print(models.rectangle.__doc__)
    print("----------")
    print(Square.__doc__)
    print(models.square.__doc__)
    