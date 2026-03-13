"""
task25_rogue_ap_detector.py

Detect rogue access points (duplicate SSID).
"""

import CoreWLAN
from collections import defaultdict


def scan_networks():

    iface = CoreWLAN.CWInterface.interface()

    networks, err = iface.scanForNetworksWithName_error_(None, None)

    ssid_map = defaultdict(list)

    for net in networks:

        ssid = net.ssid() or "Hidden"

        bssid = net.bssid()

        rssi = net.rssiValue()

        ssid_map[ssid].append((bssid, rssi))

    return ssid_map


def detect_rogue(ssid_map):

    print("\nWiFi Networks Analysis")
    print("----------------------------------")

    for ssid, access_points in ssid_map.items():

        print(f"\nSSID: {ssid}")

        for bssid, rssi in access_points:

            print(f"  BSSID: {bssid} | Signal: {rssi} dBm")

        if len(access_points) > 1:

            print("  ⚠️ Possible Rogue Access Point Detected!")


def main():

    networks = scan_networks()

    detect_rogue(networks)


if __name__ == "__main__":
    main()
