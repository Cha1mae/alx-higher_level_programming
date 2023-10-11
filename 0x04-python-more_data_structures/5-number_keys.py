#!/usr/bin/python3
def number_keys(a_dictionary):
    it_num = 0
    list_keys = list(a_dictionary.keys())

    for p in list_keys:
        it_num += 1

    return (it_num)
