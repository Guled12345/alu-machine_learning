#!/usr/bin/env python3

"""
Using the GitHub API, this script prints the location of a specific user.
"""

import requests
import sys
import time

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./2-user_location.py <GitHub API URL>")
        sys.exit(1)

    res = requests.get(sys.argv[1])

    if res.status_code == 403:
        rate_limit = int(res.headers.get('X-Ratelimit-Reset', 0))
        current_time = int(time.time())
        diff = (rate_limit - current_time) // 60
        print(f"Reset in {diff} min")

    elif res.status_code == 404:
        print("Not found")

    elif res.status_code == 200:
        data = res.json()
        print(data.get('location', 'Location not available'))
