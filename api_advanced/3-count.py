#!/usr/bin/python3
"""Recursively count keywords in the titles of a subreddit's hot posts."""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """Print a sorted count of the given keywords in hot post titles."""
    if counts is None:
        word_list = [word.lower() for word in word_list]
        counts = {word: 0 for word in word_list}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu-scripting:v1.0 (by /u/alu_student)"}
    params = {"limit": 100, "after": after}
    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        if response.status_code != 200:
            return
        data = response.json().get("data", {})
    except Exception:
        return
    for post in data.get("children", []):
        title = post.get("data", {}).get("title", "")
        for token in title.lower().split():
            if token in counts:
                counts[token] += word_list.count(token)
    after = data.get("after")
    if after is not None:
        return count_words(subreddit, word_list, after, counts)
    results = sorted(((w, c) for w, c in counts.items() if c > 0),
                     key=lambda item: (-item[1], item[0]))
    for word, count in results:
        print("{}: {}".format(word, count))
