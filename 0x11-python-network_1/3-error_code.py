#!/usr/bin/python3
"""
This script takes a URL as input, sends a request
and displays the body of the response

It takes urllib.error.HTTPError and prints: "Error code:"
followed byHTTP status code
"""

import sys
import urllib.request
import urllib.error


def wrini_hnt_idik(url):
    """
    Sends a request to the specified URL and prints the content
    If error occurs, it printserror cod
    """
    try:
        with urllib.request.urlopen(url) as response:
            html = response.read()
            print(html.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)


if __name__ == "__main__":
    """Get the URL from command-line and display the res"""
    url = sys.argv[1]
    wrini_hnt_idik(url)
