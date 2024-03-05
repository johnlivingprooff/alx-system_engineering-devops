#!/usr/bin/python3
"""Prints titles of the first 10 hot posts listed for a given subreddit."""
import requests


def top_ten(subreddit):
    """Prints titles of the first 10 hot posts listed for a given subreddit."""
    uri = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        'User-Agent': 'myBrowser/20.15.4548 (Ubuntu 18.04)'
    }
    params = {
        'limit': 10
    }

    try:
        resp = requests.get(uri, headers=headers, params=params,
                            allow_redirects=False)
        data = resp.json()

        if 'data' in data and 'children' in data['data']:
            for child in data['data']['children']:
                print(child['data']['title'])
        else:
            print(None)
    except Exception:
        print(None)
