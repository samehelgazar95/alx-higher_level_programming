#!/usr/bin/python3
""" Print the boyd and the error code """
from sys import argv
from urllib.request import urlopen
from urllib.error import HTTPError


def body_or_error(url):
    """
    Printing the body or the error code
    Argument:
        url: the url to use
    """
    try:
        with urlopen(url) as res:
            temp = res.read()
            data = temp.decode("UTF-8")
            print(data)
    except HTTPError as e:
        print('Error Code: ', e.status)


if __name__ == '__main__':
    body_or_error(argv[1])
