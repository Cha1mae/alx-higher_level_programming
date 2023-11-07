#!/usr/bin/python3
"""
using write file module
"""


def write_file(filename="", text=""):
    """
    returns the number of characters written in (UTF8) file
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        return file.write(text)


if __name__ == "__main__":
    write_file("my_first_file.txt", "This School is so cool!\n")
