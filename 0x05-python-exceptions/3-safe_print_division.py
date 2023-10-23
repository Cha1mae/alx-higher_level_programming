#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        calc_div = a / b
    except ZeroDivisionError:
        calc_div = None
    finally:
        print("Inside result: {}".format(calc_div))
        return calc_div
