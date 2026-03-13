"""
task07_detect_router.py

Question 7:
How to detect router IP automatically using Python?

This script:
1. Detects router IP address
2. Performs ARP request to get router MAC
3. Identifies router vendor
"""

from scapy.all import ARP, Ether, srp
from mac_vendor_lookup import MacLookup
from utils.network_utils import get_router_ip


def get_router_mac(router_ip: str):
    """
    Get MAC address of router using ARP request.
    """

    arp_request = ARP(pdst=router_ip)

    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")

    packet = broadcast / arp_request

    result = srp(packet, timeout=2, verbose=False)[0]

    for sent, received in result:
        return received.hwsrc

    return None


def detect_vendor(mac: str):
    """
    Detect vendor using MAC address.
    """

    try:
        return MacLookup().lookup(mac)
    except:
        return "Unknown"


def main():

    router_ip = get_router_ip()

    router_mac = get_router_mac(router_ip)

    vendor = detect_vendor(router_mac) if router_mac else "Unknown"

    print("Router Information")
    print("-----------------------------")

    print("Router IP  :", router_ip)
    print("Router MAC :", router_mac)
    print("Vendor     :", vendor)


if __name__ == "__main__":
    main()
