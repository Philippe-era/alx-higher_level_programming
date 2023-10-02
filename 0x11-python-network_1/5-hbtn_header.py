#!/usr/bin/python3
"""Shows the information relevant to the question at hand"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    read_info = requests.get(url)
    print(read_info.headers.get("X-Request-Id"))
