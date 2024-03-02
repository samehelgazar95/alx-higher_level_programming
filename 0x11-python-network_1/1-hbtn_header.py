#!/usr/bin/python3
""" Return the X-Request-Id header """
from urllib.request import urlopen
from sys import argv


with urlopen(argv[1]) as res:
    print(res.headers['X-Request-Id'])
