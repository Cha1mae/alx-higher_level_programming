#!/usr/bin/python3
"""
This takes URL as in, sends a request, then displays
the value of the X-Request-Id found in the header.
"""

import urllib.request
import sys

"""Checks if the script is executed directly"""
if __name__ == "__main__":
    """Opens a connection to the URL provided as args"""
    with urllib.request.urlopen(sys.argv[1]) as response:
        """Retrieve and print the value of the X-Request-Id from header"""
        print(response.getheader('X-Request-Id'))
