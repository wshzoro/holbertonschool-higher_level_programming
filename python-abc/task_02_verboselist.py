#!/usr/bin/env python3

class VerboseList(list):
    """
    A custom list class that extends the built-in list.
    Prints messages when items are added or removed.
    """

    def append(self, item):
        """
        Add an item to the list and print a message.
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """
        Extend the list with elements from the iterable and print a message.
        """
        count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        """
        Remove the first occurrence of item from the list and print a message.
        """
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """
        Remove and return the item at the given position and print a message.
        """
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
