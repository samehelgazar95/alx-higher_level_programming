#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

bg = BaseGeometry()

# bg.integer_validator(None, 2)
# bg.integer_validator("", 2)
bg.integer_validator("Hello", (1, 2))



