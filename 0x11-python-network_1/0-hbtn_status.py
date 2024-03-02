#!/usr/bin/python3
"""Fetching URL using urllib"""
from urllib.request import urlopen


url = "https://alx-intranet.hbtn.io/status"
with urlopen(url) as res:
    content = res.read()
    html = content.decode("UTF-8")
    msg = """Body response:
    - type: {}
    - content: {}
    - utf8 content: {}""".format(type(content), content, html)
    print(msg)
