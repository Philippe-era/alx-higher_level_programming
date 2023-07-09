#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

background = BaseGeometry()

background.integer_validator("my_int", 12)
background.integer_validator("width", 89)

try:
    background.integer_validator("name", "John")
except Exception as exc:
    print("[{}] {}".format(exc.__class__.__name__, exc))

try:
    background.integer_validator("age", 0)
except Exception as exc:
    print("[{}] {}".format(exc.__class__.__name__, exc))

try:
    background.integer_validator("distance", -4)
except Exception as exc:
    print("[{}] {}".format(exc.__class__.__name__, exc))
