#!/usr/bin/python3
"""Module to query the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit."""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Returns a list containing the titles of
    all hot articles for a given subreddit."""
    uri = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        'User-Agent': 'myBrowser/20.15.4548 (Ubuntu 18.04)'
    }
    params = {
        'limit': 100,
        'after': after
    }

    try:
        resp = requests.get(uri, headers=headers, params=params,
                            allow_redirects=False)
        data = resp.json()

        if 'data' in data and 'children' in data['data']:
            for child in data['data']['children']:
                hot_list.append(child['data']['title'])
            after = data['data']['after']
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return None
    except Exception:
        return None
