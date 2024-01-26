#!/usr/bin/python3
"""lets try a simplified code instead
of my long ones"""
import requests
import sys

if __name__ == "__main__":
    """Retrieves the URL mn the CL arg"""
    url = sys.argv[1]

    """GET the URL"""
    res = requests.get(url)

    """Retrieve d value of X header"""
    x_request_id = res.headers.get('X-Request-Id')

    """Displays the value of X  header"""
    print(x_request_id)
