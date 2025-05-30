#!/usr/bin/env python3

import math
from abc import ABC, abstractmethod


def shape_info(shape):
    """
    Prints the area and perimeter of a shape.
    Assumes the object has area() and perimeter() methods.
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))


class Shape(ABC):
    """
    Abstract base class for shapes.
    """

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """
    Circle shape.
    """

    def __init__(self, radius):
        self.radius = abs(radius)

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Rectangle shape.
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
