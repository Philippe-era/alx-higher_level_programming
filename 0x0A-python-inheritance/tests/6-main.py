#!/usr/bin/python3
BaseGeometry = __import__('6-base_geometry').BaseGeometry

background_check = BaseGeometry()

try:
    print(background_check.area())
except Exception as exc:
    print("[{}] {}".format(exc.__class__.__name__, exc))
