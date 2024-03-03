#!/usr/bin/python3
""" Returning commits <SHA>: <COMMITTER>"""
from sys import argv
from requests import get


def get_commits(repo, owner):
    url = 'https://api.github.com/repos/{}/{}/commits'.format(
        owner, repo
    )
    req = get(url)

    try:
        req_json = req.json()
        i = 0
        for item in req_json[-10:]:
            print(i)
            i = i + 1
            print('{}: {}'.format(
                item['sha'], item['commit']['author']['name'])
            )
    except Exception as e:
        print(e)


if __name__ == "__main__":
    get_commits(argv[1], argv[2])
