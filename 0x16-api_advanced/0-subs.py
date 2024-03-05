#!/usr/bin/python3
"""Module to query the Reddit API and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """Return the number of subscribers"""
    uri = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        'User-Agent': 'myBrowser/20.15.4548 (Ubuntu 18.04)'
    }

    try:
        resp = requests.get(uri, headers=headers, allow_redirects=False)
        data = resp.json()

        if 'data' in data and 'subscribers' in data['data']:
            return data.get('data').get('subscribers')
        else:
            return 0
    except Exception:
        return 0
