#!/usr/bin/python3
"""
This retrieves the status from https://alx-intranet.hbtn.io/status
using the urllib package.
"""

import urllib.request

"""Open a connection to the URL"""
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    """Read the content of the response"""
    html = response.read()

    """Display the body response information"""
    print("Body response:")
    print("\t- type:", type(html))
    print("\t- content:", html)
    print("\t- utf8 content:", html.decode('utf-8'))
