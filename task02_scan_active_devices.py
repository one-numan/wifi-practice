"""
task02_scan_active_devices.py

Question 2:
How to scan active devices in the current WiFi network using Python?

This script:
1. Detects the current network range automatically
2. Uses Nmap to perform a ping scan
3. Prints all active devices (IP addresses)

The network range is dynamically calculated using the
get_network_info() utility function.
"""

import nmap
from utils.network_utils import get_network_info


def scan_active_devices(network_range: str) -> list:
    """
    Scan the network and return active device IPs.

    Parameters
    ----------
    network_range : str
        Network CIDR range (example: 10.42.58.0/24)

    Returns
    -------
    list
        List of active device IP addresses.
    """

    scanner = nmap.PortScanner()

    # -sn means ping scan (detect active hosts only)
    scanner.scan(hosts=network_range, arguments="-sn")

    active_devices = []

    for host in scanner.all_hosts():
        active_devices.append(host)

    return active_devices


def main():
    """
    Main program execution.
    Detects network range and scans for active devices.
    """

    # Get network information dynamically
    network_info = get_network_info()

    network_range = network_info["network"]

    print("Scanning Network:", network_range)
    print("--------------------------------")

    devices = scan_active_devices(network_range)

    print("Active Devices")
    print("--------------------------------")

    for device in devices:
        print(device)


if __name__ == "__main__":
    main()