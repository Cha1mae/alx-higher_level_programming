#!/usr/bin/python3
"""Json rules"""
import requests
import sys

if __name__ == "__main__":
    """
    Retrieve the letter from CL arg
    or empty string if not provided
    """
    q = sys.argv[1] if len(sys.argv) > 1 else ""

    """SPOST API with q"""
    res = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})

    try:
        """Parse the response as JSON"""
        jres = res.json()

        """ Verify is JSON is valid (not empty)"""
        if jres:
            print("[{}] {}".format(jres['id'], jres['name']))
        else:
            print("No result")
    except ValueError:
        """Error message if the JSON is not valid"""
        print("Not a valid JSON")
