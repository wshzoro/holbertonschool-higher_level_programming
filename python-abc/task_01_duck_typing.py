#!/usr/bin/env python3
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract base class representing a geometric shape.
    Subclasses must implement the area and perimeter methods.
    """

    @abstractmethod
    def area(self):
        """
        Calculate and return the area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Calculate and return the perimeter of the shape.
        """
        pass


class Circle(Shape):
    """
    Circle shape class that inherits from Shape.
    """

    def __init__(self, radius):
        """
        Initialize a Circle with the given radius.
        """
        self.radius = radius

    def area(self):
        """
        Return the area of the circle using the formula: π * r^2
        """
        return math.pi * self.radius ** 2

    def perimeter(self):
        """
        Return the perimeter (circumference)
        of the circle using the formula: 2 * π * r
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Rectangle shape class that inherits from Shape.
    """

    def __init__(self, width, height):
        """
        Initialize a Rectangle with the given width and height.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Return the area of the rectangle using the formula: width * height
        """
        return self.width * self.height

    def perimeter(self):
        """
        Return the perimeter of the rectangle
        using the formula: 2 * (width + height)
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Print the area and perimeter of any object that behaves like a Shape.
    Uses duck typing: assumes the object has area() and perimeter() methods.
    """
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
