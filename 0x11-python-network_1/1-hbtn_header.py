#!/usr/bin/python3
"""Display the value of X-Request-Id from header"""

from urllib import request
import sys

url = sys.argv[1]

req = request.Request(url)
with request.urlopen(req) as res:
    res_id = res.headers["X-Request-Id"]

if __name__ == "__main__":
    print(res_id)
