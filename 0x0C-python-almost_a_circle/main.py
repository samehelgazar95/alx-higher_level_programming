#!/usr/bin/python3
from models.base import Base
import models.base

if __name__ == '__main__':
    b = Base()
    print(b.__doc__)
    print(models.base.__doc__)
    