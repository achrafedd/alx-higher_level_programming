#!/usr/bin/python3
"""This script fetch data from https://alx-intranet.hbtn.io/status"""

from urllib import request

url = 'https://alx-intranet.hbtn.io/status'

with request.urlopen(url) as req:
    html = req.read()

utf8 = html.decode("utf-8")

print("Body response:")
print(f"\t- type: {type(html)}")
print(f"\t- content: {html}")
print(f"\t- utf8 content: {utf8}")
