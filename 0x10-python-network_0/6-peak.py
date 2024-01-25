#!/usr/bin/python3
""" Module to find a peak num in a list of unsorted ints"""


def find_peak(list_of_integers):
    """the function will do the job for us"""
    if not list_of_integers:
        return None

    lw, hi = 0, len(list_of_integers) - 1

    while lw < hi:
        mid = (lw + hi) // 2
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            hi = mid
        else:
            lw = mid + 1

    return list_of_integers[lw]
