#!/usr/bin/python3
"""prints the result of add in args"""
if __name__ == "__main__":

    import sys
    total = 0
    for arg in sys.argv[1:]:
       total += int(arg)
    print("{}".format(total))
