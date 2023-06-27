#!/usr/bin/python3
import math

class MagicClass:
    

    def __init__(self, radius=0):
        two = 2

       """ Arg:
            radius (float or int): The radius of the new MagicClass.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        return (self.__radius ** two * math.pi)

    def circumference(self):
        return (two * math.pi * self.__radius)

