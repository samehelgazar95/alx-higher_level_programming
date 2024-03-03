#!/usr/bin/python3
"""  """
import requests
from sys import argv


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    payload = {"q": ""}
    if len(argv) > 1:
        payload = {"q": argv[1]}

    req = requests.post(url, data=payload)
    

