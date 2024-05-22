#!/usr/bin/python3
"""
contains the MyList class
"""


class MyList(list):
    """A subclass of list with a method to print the list sorted in ascending order."""

    def print_sorted(self):
        """Prints the list sorted in ascending order."""
        print(sorted(self))
