#!/usr/bin/python3
""" Module to find a peak num in a list of unsorted ints"""


def find_peak(list_of_integers):
    """the function will do the job for us"""
    if not list_of_integers:
        return None

    length = len(list_of_integers)
    if length == 1:
        return list_of_integers[0]
    elif length == 2:
        return max(list_of_integers)

    m = length // 2
    p = list_of_integers[m]
    if p > list_of_integers[m - 1] and p > list_of_integers[m + 1]:
        return p
    elif p < list_of_integers[m - 1]:
        return find_peak(list_of_integers[:m])
    else:
        return find_peak(list_of_integers[m + 1:])
