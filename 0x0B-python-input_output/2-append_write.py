#!/usr/bin/python3
"""
using append_write
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8)
    and returns the num of chars added
    """
    with open(filename, mode='a', encoding='utf-8') as file:
        return file.write(text)


if __name__ == "__main__":
    append_write("file_append.txt", "This School is so cool!\n")
