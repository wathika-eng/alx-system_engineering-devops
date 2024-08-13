#!/usr/bin/python3

import requests


def count_words(subreddit, word_list):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code != 200:
            return None

        data = response.json().get("data")
        if data:
            posts = data.get("children", [])
            for i in range(min(10, len(posts))):
                hot_list.append(posts[i]["data"]["title"])
            return recurse(subreddit, hot_list)
        else:
            return None
    except Exception:
        return None
