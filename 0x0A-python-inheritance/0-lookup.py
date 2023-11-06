#!/usr/bin/python3
"""lookup module"""


def lookup(obj):
    """Returns the list of available attributes and methods of an obj
    ARGS:
            obj: object of the list
    RETURNS:
             list: list of attribution
    """
    return dir(obj)
