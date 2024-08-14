#!/usr/bin/python3
"""
Function to count words in all hot posts of a given Reddit subreddit.
"""
import requests


def count_words(subreddit, word_list, instances=None, after="", count=0):
    """
    Prints counts of given words found in hot posts of a given subreddit.

    Args:
        subreddit (str): The subreddit to search.
        word_list (list): The list of words to search for in post titles.
        instances (dict): Key/value pairs of words/counts.
        after (str): The parameter for the next page of the API results.
        count (int): The parameter of results matched thus far.
    """
    if instances is None:
        instances = {}

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
        results = response.json().get("data", {})
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            print(f"Subreddit '{subreddit}' not found.")
        else:
            print(f"HTTP error occurred: {http_err}")
        return
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
        return
    except ValueError:
        print("Error processing JSON response")
        return

    after = results.get("after")
    count += results.get("dist", 0)

    for c in results.get("children", []):
        title = c.get("data", {}).get("title", "").lower().split()
        for word in word_list:
            word_lower = word.lower()
            occurrences = title.count(word_lower)
            if occurrences > 0:
                instances[word] = instances.get(word, 0) + occurrences

    if after:
        count_words(subreddit, word_list, instances, after, count)
    else:
        if instances:
            sorted_instances = sorted(instances.items(), key=lambda kv: (-kv[1], kv[0]))
            for word, count in sorted_instances:
                print(f"{word}: {count}")
        else:
            print("")


if __name__ == "__main__":
    # Example usage:
    subreddit = "python"
    word_list = ["Python", "requests", "API"]
    count_words(subreddit, word_list)
