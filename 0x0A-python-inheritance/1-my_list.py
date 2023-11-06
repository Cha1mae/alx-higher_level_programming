#!/usr/bin/python3
"""
MyList module
"""


class MyList(list):
    """Class that inherits from list"""

    def print_sorted(self):
        """Prints the list, but sorted (ascending)"""
        print(sorted(self))
