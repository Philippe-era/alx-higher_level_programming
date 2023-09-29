#!/usr/bin/python3
"""Handles Requests sent
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    read_info = requests.get(url)
    if read_info.status_code >= 400:
        print("Error code: {}".format(read_info.status_code))
    else:
        print(read_info.text)

