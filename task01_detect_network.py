"""
task01_detect_network.py

Question 1:
How to detect the WiFi network IP range using Python?

This script:
1. Imports network utility functions
2. Detects the current device network configuration
3. Prints IP address, subnet mask, and network range
"""

from utils.network_utils import get_network_info


def main():
    """
    Main execution function.
    Prints detected network details.
    """

    # Get network information from utility function
    network_info = get_network_info()

    print("Network Information")
    print("----------------------------")

    print("Device IP Address :", network_info["ip"])
    print("Subnet Mask       :", network_info["netmask"])
    print("Network Range     :", network_info["network"])


if __name__ == "__main__":
    main()