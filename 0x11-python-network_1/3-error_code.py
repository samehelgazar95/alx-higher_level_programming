#!/usr/bin/python3
""" Print the body and the error code """


if __name__ == "__main__":
    from sys import argv
    from urllib import request, error

    try:
        with request.urlopen(argv[1]) as res:
            print(res.read().decode('UTF-8'))
    except error.HTTPError as e:
        print('Error Code:', e.code)
