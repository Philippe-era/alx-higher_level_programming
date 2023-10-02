#!/usr/bin/python3
"""This will fetch the api"""
import urllib.request


if __name__ == "__main__":
    request = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(request) as response:
        body_fetch = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body_fetch)))
        print("\t- content: {}".format(body_fetch))
        print("\t- utf8 content: {}".format(body_fetch.decode("utf-8")))
