#!/usr/bin/python3
"""
this script fetch data from
https://alx-intranet.hbtn.io/status
"""

import requests

if __name__ == "__main__":

    url = "https://alx-intranet.hbtn.io/status"
    res = requests.get(url).content.decode('utf-8')
    print("Body response:")
    print(f"\t- type: {type(res)}")
    print(f"\t- content: {res}")
