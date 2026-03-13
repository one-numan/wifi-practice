"""
task04_detect_mac.py

Question 4:
How to detect MAC addresses of devices in the current network using Python?

This script:
1. Automatically detects the network range
2. Sends ARP broadcast packets
3. Receives responses from devices
4. Extracts IP and MAC address of devices
"""

from scapy.all import ARP, Ether, srp
from utils.network_utils import get_network_info


def arp_scan(network_range: str) -> list:
    """
    Perform ARP scan on the network.

    Parameters
    ----------
    network_range : str
        Network range in CIDR format (example: 10.42.58.0/24)

    Returns
    -------
    list
        List of dictionaries containing:
        - IP address
        - MAC address
    """

    # Create ARP request packet
    arp_request = ARP(pdst=network_range)

    # Create Ethernet broadcast packet
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")

    # Combine packets
    packet = broadcast / arp_request

    # Send packet and capture responses
    result = srp(packet, timeout=2, verbose=False)[0]

    devices = []

    for sent, received in result:
        devices.append({
            "ip": received.psrc,
            "mac": received.hwsrc
        })

    return devices


def main():
    """
    Main function to perform ARP scan and print device list.
    """

    network_info = get_network_info()

    network_range = network_info["network"]

    print("Scanning Network:", network_range)
    print("--------------------------------")

    devices = arp_scan(network_range)

    print("Discovered Devices")
    print("--------------------------------")

    for device in devices:
        print(f"IP Address : {device['ip']}")
        print(f"MAC Address: {device['mac']}")
        print("--------------------------------")


if __name__ == "__main__":
    main()