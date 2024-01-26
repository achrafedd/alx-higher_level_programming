#!/usr/bin/python3
"""
This script
"""
import sys
import requests

if __name__ == "__main__":

    url = f"https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits"
    res = requests.get(url)
    try:
        for i in range(10):
            print(f"{res.json()[i]['sha']}: {res.json()[i]['commit']['author']['name']}")
    except IndexError:
        pass
