#!/usr/bin/python3
"""  """
from urllib.request import urlopen
from urllib.parse import urlencode
from sys import argv


if __name__ == '__main__':
    email = {'email': argv[2]}
    params = urlencode(email)
    url = argv[1] + '?' + params
    with urlopen(url) as res:
        data = res.read()
        html = data.decode('UTF-8')
        print(html)
