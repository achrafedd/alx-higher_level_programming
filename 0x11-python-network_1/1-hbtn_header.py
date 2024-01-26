#!/usr/bin/python3
"""Display the value of X-Request-Id from header"""

from urllib import request
import sys

url = sys.argv[1]

with request.urlopen(url) as req:
    print(req.headers["X-Request-Id"])
