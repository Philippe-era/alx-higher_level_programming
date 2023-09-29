#!/usr/bin/python3
"""Post Request for the information
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    read_info = requests.post(url, data=value)
    print(read_info.text)

