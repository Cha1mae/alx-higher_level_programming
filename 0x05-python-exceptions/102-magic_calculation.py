#!/usr/bin/python3
def magic_calculation(a, b):
    rizz = 0
    for cv in range(1, 3):
        try:
            if cv > a:
                raise Exception('Too far')
        except:
            pass
        rizz = (b ** a) / cv + rizz
    rizz = a + b + rizz
    return rizz
