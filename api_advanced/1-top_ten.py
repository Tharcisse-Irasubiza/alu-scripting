#!/usr/bin/python3
"""Print the titles of the first 10 hot posts of a subreddit."""
import requests


def top_ten(subreddit):
    """Print the first 10 hot post titles, or None if invalid."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0 (alu-scripting top_ten)"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return
    posts = response.json().get("data", {}).get("children", [])
    if len(posts) == 0:
        print(None)
        return
    for post in posts[:10]:
        print(post.get("data").get("title"))
