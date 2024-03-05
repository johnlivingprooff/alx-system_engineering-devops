#!/usr/bin/python3
"""Module to query the Reddit API and returns a list"""
import requests


def count_words(subreddit, word_list, word_count={}, after=None):
    """Returns a list containing the titles of
    all hot articles for a given subreddit."""
    uri = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'myBrowser/20.15.4548 (Ubuntu 18.04)'}
    params = {'limit': 100, 'after': after}

    try:
        resp = requests.get(uri, headers=headers, params=params,
                            allow_redirects=False)
        data = resp.json()

        if 'data' in data and 'children' in data['data']:
            for child in data['data']['children']:
                title = child['data']['title']
                for word in word_list:
                    if word.lower() in title.lower():
                        word_count[word] = word_count.get(word, 0) + 1

            after = data['data']['after']
            if after:
                return count_words(subreddit, word_list, word_count, after)
            else:
                print_word_count(word_count)
        else:
            print("")

    except Exception as e:
        print("")


def print_word_count(word_count):
    """Prints word counts in sorted order"""
    if word_count:
        for word in sorted(word_count.keys()):
            print(f"{word}: {word_count[word]}")
    else:
        print("")
