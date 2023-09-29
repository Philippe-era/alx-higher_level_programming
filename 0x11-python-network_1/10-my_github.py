#!/usr/bin/python3
"""Github to display information required
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    read_info = requests.get("https://api.github.com/user", auth=auth)
    print(read_info.json().get("id"))

