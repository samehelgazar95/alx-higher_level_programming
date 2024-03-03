#!/usr/bin/python3
"""
Use Github API to display the id
"""
import requests
from sys import argv


def display_id(user, pwd):
    url = 'https://api.github.com/users/{}/{}'.format(user, pwd)
    req = requests.get(url, auth=(user, pwd))

    req_json = req.json()
    print(req_json['id'])


if __name__ == "__main__":
    display_id(argv[1], argv[2])
