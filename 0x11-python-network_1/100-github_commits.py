#!/usr/bin/python3
""" Returning commits <SHA>: <COMMITTER>"""
from sys import argv
from requests import get


def get_commits(repo, owner):
    url = 'https://api.github.com/repos/{}/{}/commits'.format(
        owner, repo
    )
    req = get(url)
    req_json = req.json()
    
    for item in req_json:
        print(item['sha'])
        print(item['commit']['author']['name'])
        print("")
    
if __name__ == "__main__":
    get_commits(argv[1], argv[2])