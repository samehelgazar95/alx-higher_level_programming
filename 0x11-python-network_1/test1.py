#!/usr/bin/python3
"""Fetching URL using urllib"""
from urllib.request import urlopen 


url = "https://alx-intranet.hbtn.io/status"
with urlopen(url) as res:
    print(dir(res))
    print("Status: ", res.status)
    print("Code: ", res.code)
    print("Version: ", res.version)
    print("Length: ", res.length)

    print("Content peek: ", res.peek())
    print("res Type: ", type(res))

    data = res.read()
    print("Content read: ", data)
    print("data Type: ", type(data))

    html = data.decode("UTF-8")
    print("HTML: ", html)
    print("HTML Type: ", type(html))

