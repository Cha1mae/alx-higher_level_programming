#!/usr/bin/python3
"""locked class def"""


class LockedClass:
    """
    Create a LockedClass that prohibits the creation
    of new instance attributes, except
    for the 'first_name' attribute
    """
    __slots__ = 'first_name'
