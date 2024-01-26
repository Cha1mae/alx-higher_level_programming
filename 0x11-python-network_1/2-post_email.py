#!/usr/bin/python3
"""
This script takes a URL and an email as input,
sends a POST request to the URL with the email as a parameter,
then it  displays the response
"""

import urllib.request
import urllib.parse
import sys

""" Checks if the script is directlye xecuted """
if __name__ == "__main__":
    """ Gets the URL and email"""
    url = sys.argv[1]
    email = sys.argv[2]

    """ Prepares the data to be sent in a POST"""
    values = {'email': email}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')

    """ Creates a request obj with the URL and data """
    req = urllib.request.Request(url, data)

    """ Opens a connection to the URL"""
    with urllib.request.urlopen(req) as response:
        """ Displays the body of the response"""
        print(response.read().decode('utf-8'))
