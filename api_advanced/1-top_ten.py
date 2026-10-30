#!/usr/bin/python3
"""Print the titles of the first 10 hot posts of a subreddit."""
import requests


def top_ten(subreddit):
    """Print the first 10 hot post titles of a subreddit, then OK."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu-scripting:v1.0 (by /u/alu_student)"}
    params = {"limit": 10}
    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False, timeout=10)
        if response.status_code == 200:
            posts = response.json().get("data", {}).get("children", [])
            for post in posts[:10]:
                print(post.get("data", {}).get("title"))
    except (requests.RequestException, ValueError):
        pass
    print("OK", end="")
