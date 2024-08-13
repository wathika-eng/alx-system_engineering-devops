#!/usr/bin/python3

import requests


def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code != 200:
            print(None)
            return

        data = response.json().get("data")
        if data:
            posts = data.get("children", [])
            for i in range(min(10, len(posts))):
                print(posts[i]["data"]["title"])
        else:
            print(None)
    except Exception:
        print(None)
