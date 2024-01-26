#!/usr/bin/python3
"""if this works it will be so cool"""
import requests
import sys

if __name__ == "__main__":
    """Check if the correct number of CL arguments provided"""
    if len(sys.argv) != 3:
        print("Usage: ./10-my_github.py <username> <token>")
        sys.exit(1)

    """Retrieves my GitHub credentials from CL"""
    username = sys.argv[1]
    token = sys.argv[2]

    """GET the GitHub API using authentication"""
    res = requests.get('https://api.github.com/user', auth=(username, token))

    """Displays the user id or None"""
    if res.status_code == 200:
        print(res.json().get('id'))
    else:
        print(None)
