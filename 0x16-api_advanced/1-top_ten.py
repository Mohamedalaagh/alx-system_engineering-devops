#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "limit": 10
    }
    
    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        response.raise_for_status()
    except requests.RequestException as e:
        print("None")
        return

    try:
        results = response.json().get("data", {}).get("children", [])
        if not results:
            print("None")
            return
        for post in results:
            title = post.get("data", {}).get("title")
            if title:
                print(title)
    except ValueError:
        print("None")
