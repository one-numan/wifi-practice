"""
task16_wifi_movement_tracker.py

Track WiFi signal changes and detect movement
towards or away from the router.
"""

import time
from task14_wifi_rssi import get_wifi_info
from task15_wifi_distance import estimate_distance


def detect_movement(previous_rssi, current_rssi):
    """
    Detect movement direction based on RSSI change.
    """

    if current_rssi > previous_rssi:
        return "Moving Closer"

    elif current_rssi < previous_rssi:
        return "Moving Away"

    else:
        return "Stable"


def main():

    print("Starting WiFi Movement Tracker...\n")

    previous_rssi = None

    while True:

        ssid, rssi = get_wifi_info()

        rssi = int(rssi)

        distance = estimate_distance(rssi)

        if previous_rssi is None:
            movement = "Initializing"
        else:
            movement = detect_movement(previous_rssi, rssi)

        print("------------------------------")
        print("SSID :", ssid)
        print("RSSI :", rssi, "dBm")
        print("Distance :", distance, "meters")
        print("Movement :", movement)

        previous_rssi = rssi

        time.sleep(3)


if __name__ == "__main__":
    main()
