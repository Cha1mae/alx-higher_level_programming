#!/usr/bin/python3
"""error :("""
import sys
import requests

if __name__ == "__main__":
    """Retrieves the URL"""
    url = sys.argv[1]

    """GET URL, nothing to explain here"""
    res = requests.get(url)

    """Checks HTTP status code then displays the response"""
    if res.status_code < 400:
        print(res.text)
    else:
        print("Error code: {}".format(res.status_code))
