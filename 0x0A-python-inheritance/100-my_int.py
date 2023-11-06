#!/usr/bin/python3
"""My integer module"""


class MyInt(int):
    """Class MyInt that inherits from int"""

    def __eq__(self, other):
        """Inverted behavior of the == operator"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Inverted behavior of the != operator"""
        return super().__eq__(other)
