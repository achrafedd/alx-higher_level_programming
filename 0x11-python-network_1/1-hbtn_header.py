#!/usr/bin/python3
""" This script take url as argument and
send request to display the value of X-Request-Id"""

from urllib import request
from sys import argv

url = argv[1]

with request.urlopen(url) as req:
    print(req.headers["X-Request-Id"])
