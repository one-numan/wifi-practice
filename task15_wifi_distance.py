"""
task15_wifi_distance.py

Estimate distance from WiFi router using RSSI.
"""

import math
from task14_wifi_rssi import get_wifi_info


def estimate_distance(rssi, tx_power=-40, n=2):
    """
    Estimate distance using RSSI.

    Parameters
    ----------
    rssi : int
        Signal strength
    tx_power : int
        Signal strength at 1 meter
    n : float
        Environment factor

    Returns
    -------
    float
        Estimated distance in meters
    """

    distance = 10 ** ((tx_power - rssi) / (10 * n))

    return round(distance, 2)


def main():

    ssid, rssi = get_wifi_info()

    rssi = int(rssi)

    distance = estimate_distance(rssi)

    print("WiFi Distance Estimation")
    print("-----------------------------")

    print("SSID :", ssid)
    print("RSSI :", rssi, "dBm")
    print("Estimated Distance :", distance, "meters")


if __name__ == "__main__":
    main()
