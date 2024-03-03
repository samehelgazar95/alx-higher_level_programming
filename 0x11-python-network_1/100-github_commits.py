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
        for item in req_json[:10]:
            print('{}: {}'.format(
                item['sha'], item['commit']['author']['name'])
            )
    except Exception:
        pass


if __name__ == "__main__":
    get_commits(argv[1], argv[2])
