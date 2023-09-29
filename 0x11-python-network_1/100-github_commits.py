#!/usr/bin/python3
"""Lists repo commits
"""
import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    read_info = requests.get(url)
    commits = read_info.json()
    try:
        for initial in range(10):
            print("{}: {}".format(
                commits[initial].get("sha"),
                commits[initial].get("commit").get("author").get("name")))
    except IndexError:
        pass

