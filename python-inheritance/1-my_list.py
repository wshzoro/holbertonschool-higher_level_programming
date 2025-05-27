#!/usr/bin/python3
"""
Module 1-my_list
Contains the MyList class that inherits from list
and a method to print the list sorted without modifying it.
"""


class MyList(list):

    """
    Class that inherits from list, with a method to print the list sorted.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order
        without modifying the original list.
        """
        print(sorted(self))
