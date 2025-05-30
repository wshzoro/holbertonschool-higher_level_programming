#!/usr/bin/env python3

"""
Mixin that adds swimming ability
"""


class SwimMixin:
    def swim(self):
        """
        Print a message indicating the creature can swim
        """
        print("The creature swims!")


"""
Mixin that adds flying ability
"""


class FlyMixin:
    def fly(self):
        """
        Print a message indicating the creature can fly
        """
        print("The creature flies!")


"""
Dragon class that inherits both swimming and flying abilities
"""


class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        """
        Print a message indicating the dragon can roar
        """
        print("The dragon roars!")
