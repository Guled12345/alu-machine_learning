#!/usr/bin/env python3

"""SpaceX API script that displays information about the upcoming launch."""

import requests
from datetime import datetime

if __name__ == '__main__':
    # Fetch upcoming launches from the SpaceX API
    url = "https://api.spacexdata.com/v4/launches/upcoming"
    r = requests.get(url)

    if r.status_code != 200:
        print("Failed to retrieve data from SpaceX API")
        exit(1)

    # Identify the next launch based on the earliest timestamp
    upcoming_launch = min(r.json(), key=lambda x: int(x["date_unix"]))

    launch_name = upcoming_launch["name"]
    date = upcoming_launch["date_local"]
    rocket_id = upcoming_launch["rocket"]
    launchpad_id = upcoming_launch["launchpad"]

    # Fetch rocket information
    rocket_url = f"https://api.spacexdata.com/v4/rockets/{rocket_id}"
    rocket_name = requests.get(rocket_url).json().get("name", "Unknown Rocket")

    # Fetch launchpad information
    launchpad_url = f"https://api.spacexdata.com/v4/launchpads/{launchpad_id}"
    launchpad_data = requests.get(launchpad_url).json()
    launchpad_name = launchpad_data.get("name", "Unknown Launchpad")
    launchpad_locality = launchpad_data.get("locality", "Unknown Location")

    # Format the launch information string
    launch_info = f"{launch_name} ({date}) - {rocket_name} at {launchpad_name} ({launchpad_locality})"
    print(launch_info)
