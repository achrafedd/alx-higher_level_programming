#!/usr/bin/python3
"""
This script take 2 args repo and owner
to get all commits and display last 10
"""

import sys
import requests

if __name__ == "__main__":

    url = f"https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits"
    res = requests.get(url)
    try:
        for i in range(10):
            sha = res.json()[i]['sha']
            owner = res.json()[i]['commit']['author']['name']
            print(f"{sha}: {owner}")
    except IndexError:
        pass
