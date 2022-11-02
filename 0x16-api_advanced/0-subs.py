#!/usr/bin/python3

"""
A function that queries the Reddit API and returns
the number of subscribers (not active users, total subscribers)
for a given subreddit. If an invalid subreddit is given
the function will return 0.
"""


import requests


def number_of_subscribers(subreddit):
    """
    Query reddit API to fetch number of subscribers
    subreddit: subreddit name
    Return: Number of subscribers or 0 if invalid subreddit
    """

    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    headers = {
        "User-Agent": "Custom"
    }
    response = requests.get(url, allow_redirects=False, headers=headers)
    if response.status_code == 200:
        data = response.json().get("data").get("subscribers")
        return data
    return 0
