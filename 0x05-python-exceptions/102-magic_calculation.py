#!/usr/bin/python3
def magic_calculation(a, b):
    calc = 0
    for maj in range(1, 3):
        try:
            if maj > a:
                raise Exception('Too far')
            calc += a ** b / maj
        except Exception:
            calc = b + a
            break
    return calc
