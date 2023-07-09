#!/usr/bin/python3
Rectangle = __import__('8-rectangle').Rectangle

rect = Rectangle(3, 5)

print(rect)
print(dir(rect))

try:
    print("Rectangle: {} - {}".format(rect.width, rect.height))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    rect2 = Rectangle(4, True)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
