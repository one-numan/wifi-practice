"""
task06_device_inventory.py

Question 6:
Generate a list of connected devices in the current network.

This script:
1. Detects network range automatically
2. Performs ARP scan
3. Detects MAC address
4. Identifies vendor or randomized MAC
5. Prints device inventory table
"""

from scapy.all import ARP, Ether, srp
from mac_vendor_lookup import MacLookup
from utils.network_utils import get_network_info


def is_random_mac(mac: str) -> bool:
    """
    Detect if MAC address is locally administered (randomized).

    Parameters
    ----------
    mac : str

    Returns
    -------
    bool
    """

    first_byte = int(mac.split(":")[0], 16)

    return bool(first_byte & 2)


def detect_vendor(mac: str) -> str:
    """
    Detect vendor from MAC address.

    If MAC is randomized, return 'Randomized'.
    """

    if is_random_mac(mac):
        return "Randomized"

    try:
        return MacLookup().lookup(mac)

    except Exception:
        return "Unknown"


def arp_scan(network_range: str) -> list:
    """
    Scan network using ARP and return device inventory.
    """

    arp_request = ARP(pdst=network_range)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")

    packet = broadcast / arp_request

    result = srp(packet, timeout=2, verbose=False)[0]

    devices = []

    for sent, received in result:

        mac = received.hwsrc

        devices.append({
            "ip": received.psrc,
            "mac": mac,
            "type": detect_vendor(mac)
        })

    return devices


def print_table(devices: list):
    """
    Print device list in table format.
    """

    print("\nConnected Devices")
    print("--------------------------------------------------------")
    print(f"{'IP Address':<18}{'MAC Address':<20}{'Type'}")
    print("--------------------------------------------------------")

    for d in devices:
        print(f"{d['ip']:<18}{d['mac']:<20}{d['type']}")


def main():

    network_info = get_network_info()

    network_range = network_info["network"]

    print("Scanning Network:", network_range)

    devices = arp_scan(network_range)

    print_table(devices)


if __name__ == "__main__":
    main()