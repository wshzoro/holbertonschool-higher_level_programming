#!/usr/bin/env python3

class CountedIterator:
    """
    A custom iterator that counts how many items have been iterated over.
    """

    def __init__(self, iterable):
        """
        Initialize the CountedIterator with an iterable.
        Set up the internal iterator and the counter.
        """
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """
        Return the next item from the iterator and increment the count.
        Raise StopIteration when no more items are available.
        """
        item = next(self.iterator)  # May raise StopIteration
        self.count += 1
        return item

    def get_count(self):
        """
        Return the number of items that have been iterated over.
        """
        return self.count

    def __iter__(self):
        """
        Return the iterator object itself.
        """
        return self
