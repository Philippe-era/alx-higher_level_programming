#!/usr/bin/python3
"""Fetches information from database."""
import requests


if __name__ == "__main__":
    read_info = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(read_info.text)))
    print("\t- content: {}".format(read_info.text))

