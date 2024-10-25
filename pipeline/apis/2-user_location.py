#!/usr/bin/env python3
"""
Using the GitHub API, this script prints the location
of a specific user.
"""

import requests
import sys
import time

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./script.py <GitHub username>")
        sys.exit(1)

    username = sys.argv[1]
    url = f"https://api.github.com/users/{username}"

    try:
        res = requests.get(url)

        if res.status_code == 403:
            rate_limit = int(res.headers.get('X-RateLimit-Reset', 0))
            current_time = int(time.time())
            diff = (rate_limit - current_time) // 60
            print(f"Rate limit exceeded. Try again in {diff} min.")

        elif res.status_code == 404:
            print("User not found.")

        elif res.status_code == 200:
            data = res.json()
            location = data.get('location', 'Location not available')
            print(f"Location: {location}")

        else:
            print(f"Error: Received unexpected status code {res.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
