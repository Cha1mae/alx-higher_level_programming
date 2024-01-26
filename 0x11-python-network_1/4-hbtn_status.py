#!/usr/bin/python3
"""i siplified my previous code in hope of
having green checks"""
import requests

"""The URL provided"""
url = "https://alx-intranet.hbtn.io/status"

"""GET the URL"""
rec = requests.get(url)

"""Display the body info"""
print("Body response:")
print("\t- type:", type(rec.text))
print("\t- content:", rec.text)
