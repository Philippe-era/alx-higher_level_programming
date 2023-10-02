#!/usr/bin/python3
"""Post request to the http"""
import sys
import requests


if __name__ == "__main__":
    letter_check = "" if len(sys.argv) == 1 else sys.argv[1]
    pay = {"q": letter_check}

    read_info = requests.post("http://0.0.0.0:5000/search_user", data=pay)
    try:
        response = read_info.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
