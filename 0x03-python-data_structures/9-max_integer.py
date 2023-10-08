#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    list_copy = my_list.copy()
    list_copy.sort()
    return list_copy[-1]
