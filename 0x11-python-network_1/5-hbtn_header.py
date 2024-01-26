#!/usr/bin/python3
"""
This script displays the value of the
variable X-Request-Id in the response header
"""

import requests
import sys

if __name__ == "__main__":

    url = sys.argv[1]
    header_id = requests.get(url).headers["X-Request-Id"]
    print(header_id)
