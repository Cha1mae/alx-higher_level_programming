#!/usr/bin/python3
"""
student init json
"""


class Student:
    """
    Student class
    """

    def __init__(self, first_name, last_name, age):
        """
        def a Student instance
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictnry representation of a Student instance
        """
        return self.__dict__


if __name__ == "__main__":
    pass
