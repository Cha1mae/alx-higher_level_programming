#!/usr/bin/python3
"""lets post an email :)"""
import requests
import sys

if __name__ == "__main__":
    """Retrieve the URL and the email"""
    url = sys.argv[1]
    email = sys.argv[2]

    """Prepares the data to be POSTed"""
    D = {'email': email}

    """Send a POST to the URL with the email"""
    res = requests.post(url, data=D)

    """Displays the body ;)"""
    print("Your email is: {}".format(email))
