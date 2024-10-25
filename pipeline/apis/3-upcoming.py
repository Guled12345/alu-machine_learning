#!/usr/bin/env python3

"""SpaceX API script to display the frequency of launches by rocket type."""

import requests

if __name__ == '__main__':
    # Fetch all launches from the SpaceX API
    url = "https://api.spacexdata.com/v4/launches"
    r = requests.get(url)

    if r.status_code != 200:
        print("Failed to retrieve data from SpaceX API")
        exit(1)

    launches = r.json()
    rocket_count = {}

    # Count the number of launches per rocket type
    for launch in launches:
        rocket_id = launch["rocket"]

        # Fetch rocket name only if it's not already counted
        if rocket_id not in rocket_count:
            rocket_url = f"https://api.spacexdata.com/v4/rockets/{rocket_id}"
            rocket_name = requests.get(rocket_url).json().get("name", "Unknown Rocket")
            rocket_count[rocket_name] = 0

        rocket_count[rocket_name] += 1

    # Print the rocket types with their launch counts
    for rocket_name, count in rocket_count.items():
        print(f"{rocket_name}: {count}")
