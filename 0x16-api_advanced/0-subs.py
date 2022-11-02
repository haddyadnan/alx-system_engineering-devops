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

    response = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers={"User-Agent": "Custom"},
    )

    if response.status_code == 200:
        return response.json().get("data").get("subscribers")
    else:
        return 0
