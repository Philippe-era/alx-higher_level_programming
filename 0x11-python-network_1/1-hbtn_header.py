#!/usr/bin/python3
"""Displays the X header
"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    request_open = urllib.request_open.Request(url)
    with urllib.request_open.urlopen(request_open) as response:
        print(dict(response_open.headers).get("X-Request-Id"))

