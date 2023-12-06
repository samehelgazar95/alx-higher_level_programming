#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

bg = BaseGeometry()

bg.integer_validator("my_int", -2147483642147483647789)

try:
    bg.integer_validator("long", 2147483647)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
