#!/usr/bin/python3
"""
A function that queries the Reddit API
and prints the titles of the first 10 hot posts
listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Query reddit API to fetch top 10 hot posts
    subreddit: subreddit name
    Return: hot posts
    if invalid subreddit return None
    """

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
         Chrome/102.0.0.0 Safari/537.36"
    }
    params = {"limit": 10}

    try:
        response = requests.get(
            url, headers=headers, allow_redirects=False, params=params
        ).json()
        posts = response.get("data").get("children")
        for post in posts:
            print(post.get("data").get("title"))
    except Exception as e:
        print(e)
