#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    cool_dict = a_dictionary.copy()
    list_keys = list(cool_dict.keys())

    for i in list_keys:
        cool_dict[i] *= 2

    return (cool_dict)
