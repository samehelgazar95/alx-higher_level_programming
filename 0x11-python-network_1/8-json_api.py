#!/usr/bin/python3
""" Searching for a LOST User """
import requests
from sys import argv


def search_user(letter):
    url = "http://0.0.0.0:5000/search_user"
    payload = {"q": letter}
    req = requests.post(url, data=payload)

    if req.status_code == 200:
        try:
            req_json = req.json()
            if req_json:
                print('[{}] {}'.format(req_json['id'], req_json['name']))
            else:
                print('No result')
        except ValueError:
            print("Not a valid JSON")
    else:
        print('Error Status Code: ', req.status_code)


if __name__ == "__main__":
    letter = argv[1] if len(argv) > 1 else ""
    search_user(letter)
