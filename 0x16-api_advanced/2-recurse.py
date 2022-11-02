#!/usr/bin/python3
"""
Write a recursive function that queries the Reddit API
and returns a list containing the titles
of all hot articles for a given subreddit.
If no results are found for the given subreddit
the function returns None.
"""

import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    Query reddit API to fetch titles of hot articles
    subreddit: subreddit name
    Return: hot posts
    if invalid subreddit return None
    """

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
         Chrome/102.0.0.0 Safari/537.36"
    }
    params = {"after": after}

    try:
        response = requests.get(
            url, headers=headers, allow_redirects=False, params=params
        ).json()
        posts = response.get("data").get("children")
        for post in posts:
            hot_list.append(post.get("data").get("title"))
        after = response.get("data").get("after")
        if after is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, after)
    except Exception:
        return None
