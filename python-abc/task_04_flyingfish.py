#!/usr/bin/env python3

"""Define the Fish class with swim and habitat methods"""


class Fish:
    def swim(self):
        """Print a swimming message for a fish"""
        print("The fish is swimming")

    def habitat(self):
        """Print the typical habitat for a fish"""
        print("The fish lives in water")


"""Define the Bird class with fly and habitat methods"""


class Bird:
    def fly(self):
        """Print a flying message for a bird"""
        print("The bird is flying")

    def habitat(self):
        """Print the typical habitat for a bird"""
        print("The bird lives in the sky")


"""Define the FlyingFish class, inheriting from both Fish and Bird"""


class FlyingFish(Fish, Bird):
    def swim(self):
        """Override swim to describe how a flying fish swims"""
        print("The flying fish is swimming!")

    def fly(self):
        """Override fly to describe how a flying fish flies"""
        print("The flying fish is soaring!")

    def habitat(self):
        """Override habitat to describe where a flying fish lives"""
        print("The flying fish lives both in water and the sky!")
