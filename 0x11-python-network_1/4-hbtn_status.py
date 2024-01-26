#!/usr/bin/python3
import requests


def fetch_lurl():
    """
    Fetches the status from the link  using request
    Displays the body response with the info
    """
    """The URL provided"""
    url = "https://alx-intranet.hbtn.io/status"

    """GET the URL"""
    rec = requests.get(url)

    """Display the body info"""
    print("Body response:")
    print("\t- type:", type(rec.text))
    print("\t- content:", rec.text)


if __name__ == "__main__":
    """Call the fetch_lurl function"""
    fetch_lurl()
