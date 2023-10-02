#!/usr/bin/python3
"""A Post request is requested and filled for"""


import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url_look = sys.argv[1]
    value_check = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value_check).encode("ascii")

    request = urllib.request.Request(url_look, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
