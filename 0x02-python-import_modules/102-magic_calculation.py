#!/usr/bin/python3
"""magic calc"""
def magic_calculation(a, b):

    c = 0
    if a < b:
        add = __import__('magic_calculation_102').add
        sub = __import__('magic_calculation_102').sub
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
    else:
        c = __import__('magic_calculation_102').sub(a, b)
    return (c)
