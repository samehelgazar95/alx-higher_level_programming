#!/usr/bin/python3
""" Print the body and the error code """
from sys import argv
from urllib.request import Request, urlopen
from urllib.error import HTTPError


if __name__ == '__main__':
    try:
        with urlopen(argv[1]) as res:
            data = res.read().decode("UTF-8")
            print(data)
    except HTTPError as e:
        print('Error Code: {}'.format(e.code))
