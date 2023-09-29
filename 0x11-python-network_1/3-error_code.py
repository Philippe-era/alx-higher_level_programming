#!/usr/bin/python3
"""Given URL to look at and for
"""
import sys
import urllib.error
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    request_look = urllib.request_look.Request(url)
    try:
        with urllib.request_look.urlopen(request_look) as response:
            print(response.read().decode("ascii"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))

