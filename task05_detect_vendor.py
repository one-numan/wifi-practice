"""
task05_detect_vendor.py

Question 5:
How to identify device vendor using MAC address in Python?

This script:
1. Detects the network range automatically
2. Performs ARP scan to get IP and MAC addresses
3. Uses MAC OUI lookup to detect vendor name
"""

from scapy.all import ARP, Ether, srp
from mac_vendor_lookup import MacLookup
from utils.network_utils import get_network_info



def arp_scan(network_range: str) -> list:
    """
    Perform ARP scan and return devices with IP and MAC.

    Parameters
    ----------
    network_range : str
        CIDR network range (example: 10.42.58.0/24)

    Returns
    -------
    list
        List of dictionaries containing IP and MAC addresses.
    """

    arp_request = ARP(pdst=network_range)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")

    packet = broadcast / arp_request

    result = srp(packet, timeout=2, verbose=False)[0]

    devices = []

    for sent, received in result:
        devices.append({
            "ip": received.psrc,
            "mac": received.hwsrc
        })

    return devices


def detect_vendor(mac: str) -> str:
    """
    Detect device vendor using MAC address.

    Parameters
    ----------
    mac : str
        MAC address of the device

    Returns
    -------
    str
        Vendor name if found otherwise 'Unknown'
    """

    try:
        vendor = MacLookup().lookup(mac)
        return vendor

    except Exception:
        return "Unknown / Randomized MAC"

    return vendor


def main():
    """
    Main function that scans devices and prints vendor info.
    """

    network_info = get_network_info()

    network_range = network_info["network"]

    print("Scanning Network:", network_range)
    print("-------------------------------------")

    devices = arp_scan(network_range)

    for device in devices:

        vendor = detect_vendor(device["mac"])

        print("IP Address :", device["ip"])
        print("MAC Address:", device["mac"])
        print("Vendor     :", vendor)
        print("-------------------------------------")


if __name__ == "__main__":
    main()