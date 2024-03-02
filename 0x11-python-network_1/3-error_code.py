#!/usr/bin/python3
""" Print the body and the error code """
from sys import argv
from urllib.request import Request, urlopen
from urllib.error import HTTPError


def body_or_error(url):
    """
    Printing the body or the error code
    Argument:
        url: the url to use
    """
    try:
        req = Request(url)
        with urlopen(req) as res:
            temp = res.read()
            data = temp.decode("ascii")
            print(data)
    except HTTPError as e:
        print('Error Code: {}'.format(e.code))


if __name__ == '__main__':
    body_or_error(argv[1])
