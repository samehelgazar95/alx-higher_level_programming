#!/usr/bin/python3
"""
Use Github API to display the id
"""
from requests import get
from requests.auth import HTTPBasicAuth
from sys import argv


def display_id(user, pwd):
    url = 'https://api.github.com/user'
    req = get(url, auth=HTTPBasicAuth(user, pwd))

    req_json = req.json()
    print(req_json.get("id"))


if __name__ == "__main__":
    display_id(argv[1], argv[2])
