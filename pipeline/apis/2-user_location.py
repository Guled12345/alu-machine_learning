#!/usr/bin/env python3

"""
Using the GitHub API, this script prints the location of a specific user.
"""

import requests
import sys
import time

if __name__ == "__main__":
    # Ensure the user provides the correct argument
    if len(sys.argv) < 2:
        print("Usage: ./2-user_location.py <GitHub API URL>")
        sys.exit(1)

    # Make a request to the provided URL
    res = requests.get(sys.argv[1])

    if res.status_code == 403:
        # Handle rate limit error
        rate_limit = int(res.headers.get('X-Ratelimit-Reset', 0))
        current_time = int(time.time())
        diff = (rate_limit - current_time) // 60
        print(f"Reset in {diff} min")

    elif res.status_code == 404:
        # Handle user not found
        print("Not found")

    elif res.status_code == 200:
        # Print the user's location
        data = res.json()
        print(data.get('location', 'Location not available'))
