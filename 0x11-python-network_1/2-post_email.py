#!/usr/bin/python3
""" posting email to the url """
from urllib.request import urlopen, Request
from urllib.parse import urlencode
from sys import argv


def post_email(url, email):
    """
    Posting Email to a specific URL
    Arguments:
        url: the url to send to
        email: the email to send
    """
    try:
        params = urlencode({'email': email})
        params = params.encode('ascii')
        req = Request(url, params)
        with urlopen(req) as res:
            data = res.read()
            html = data.decode('UTF-8')
            print(html)
    except Exception as e:
        print("An error occured: {}".format(e))


if __name__ == '__main__':
    url = argv[1]
    email = argv[2]
    post_email(url, email)
