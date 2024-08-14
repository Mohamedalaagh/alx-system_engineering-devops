#!/usr/bin/python3
"""
Function to query a list of all hot posts on a given Reddit subreddit.
"""
import requests


def recurse(subreddit, hot_list=None, after="", count=0):
    """
    Returns a list of titles of all hot posts on a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): The list of hot post titles, used for recursion.
        after (str): The parameter for pagination (Reddit's 'after' token).
        count (int): The number of posts retrieved so far.

    Returns:
        list: A list of hot post titles, or None if the subreddit is invalid.
    """
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

    try:
        data = response.json().get("data", {})
        after = data.get("after")
        count += data.get("dist", 0)

        hot_list.extend([child.get("data", {}).get("title") for child in data.get("children", [])])

        if after:
            return recurse(subreddit, hot_list, after, count)
        return hot_list
    except ValueError:
        print("Error processing JSON response")
        return None
