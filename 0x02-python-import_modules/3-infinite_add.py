#!/usr/bin/python3
"""prints the result of add in args"""
if __name__ == "__main__":
    import sys

    total = 0
    for i in range(len(sys.argv) - 1):
        total += int(sys.argv[i + 1])
    print("{}".format(total))
