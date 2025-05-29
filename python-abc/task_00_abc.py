#!/usr/bin/env python3
from abc import ABC, abstractmethod
"""
Modules that Define the Animal class,
ensuring it inherits from ABC to mark it as abstract
"""


class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass


"""
Create a subclass named Dog that inherits from the Animal class
"""


class Dog(Animal):
    def sound(self):
        return "Bark"


class Cat(Animal):
    def sound(self):
        return "Meow"
