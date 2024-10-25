#!/usr/bin/env python3
"""Pipeline API"""
import requests

if __name__ == '__main__':
    """Fetch upcoming SpaceX launches."""
    url = "https://api.spacexdata.com/v4/launches/upcoming"
    r = requests.get(url)

    if r.status_code != 200:
        print("Failed to retrieve data from SpaceX API")
        exit(1)

    launches = r.json()
    recent_launch = None

    # Iterate through launches to find the earliest upcoming launch
    for launch in launches:
        if recent_launch is None or launch["date_unix"] < recent_launch["date_unix"]:
            recent_launch = launch

    # Check if a recent launch was found
    if recent_launch:
        launch_name = recent_launch["name"]
        date = recent_launch["date_local"]
        rocket_id = recent_launch["rocket"]
        launchpad_id = recent_launch["launchpad"]

        # Fetch rocket name
        rocket_url = f"https://api.spacexdata.com/v4/rockets/{rocket_id}"
        rocket_name = requests.get(rocket_url).json().get("name", "Unknown Rocket")

        # Fetch launchpad details
        launchpad_url = f"https://api.spacexdata.com/v4/launchpads/{launchpad_id}"
        launchpad = requests.get(launchpad_url).json()
        launchpad_name = launchpad.get("name", "Unknown Launchpad")
        launchpad_locality = launchpad.get("locality", "Unknown Location")

        # Format the output
        output = f"{launch_name} ({date}) {rocket_name} - {launchpad_name} ({launchpad_locality})"
        print(output)
