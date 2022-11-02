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
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/102.0.0.0 Safari/537.36'}
    try:
        response = requests.get(url, allow_redirects=False, headers=headers).json()
        data = response.get("data").get("subscribers")
        return data
    except Exception:
        return 0
