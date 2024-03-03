#!/usr/bin/python3
"""Fetching URL using urllib"""
from urllib.request import urlopen


def url_req(url):
    """"
    Requesting url
    Arguments:
        url: the url to request
    """    
    with urlopen(url) as res:
        content = res.read()
        html = content.decode("UTF-8")
        print('Body response:')
        print('\t- type: {}'.format(type(content)))
        print('\t- content: {}'.format(content))
        print('\t- utf8 content: {}'.format(html))


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    url_req(url)
