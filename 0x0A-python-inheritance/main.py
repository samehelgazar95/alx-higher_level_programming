#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

gModule = __import__("7-base_geometry").__doc__
gClass = BaseGeometry.__doc__
gArea = BaseGeometry.area.__doc__
gInt = BaseGeometry.integer_validator.__doc__

print(gModule)
print(gClass)
print(gArea)
print(gInt)
