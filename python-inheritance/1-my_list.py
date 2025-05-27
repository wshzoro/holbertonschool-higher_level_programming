#!/usr/bin/python3
"""
Contain the MyList class that inherits from list
and a method to print the list sorted without modifying it
"""
class MyList(list):
    """
    Class that inherites from list, with a method to print the list sorted
    """
    def print_sorted(self):
        """
        Prints the list in ascending sorted order without modifying theo original list
        """
        print(sorted(self))
