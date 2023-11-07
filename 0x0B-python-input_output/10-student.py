#!/usr/bin/python3
"""
Student t10 module
"""


class Student:
    """
    Student class
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance with filter
        """
        try:
            for attr in attrs:
                if type(attr) is not str:
                    return self.__dict__
        except Exception:
            return self.__dict__
        mon_dic = dict()
        for key, value in self.__dict__.items():
            if key in attrs:
                mon_dic[key] = value
        return mon_dic
