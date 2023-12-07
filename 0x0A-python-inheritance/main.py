#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

gModule = __import__("7-base_geometry").__doc__
gClass = __import__("7-base_geometry").BaseGeometry.__doc__
gArea = __import__("7-base_geometry").BaseGeometry.area.__doc__
gInt = __import__("7-base_geometry").BaseGeometry.integer_validator.__doc__

print(gModule)
print(gClass)
print(gArea)
print(gInt)
