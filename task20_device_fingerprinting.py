"""
task20_device_fingerprinting.py

Identify device type using MAC vendor and TTL.
"""

from scapy.all import ARP, Ether, srp, IP, ICMP, sr1
from mac_vendor_lookup import MacLookup


network = "192.168.1.0/24"


def scan_network():

    arp = ARP(pdst=network)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")

    packet = ether / arp

    result = srp(packet, timeout=2, verbose=False)[0]

    devices = []

    for sent, received in result:

        devices.append({
            "ip": received.psrc,
            "mac": received.hwsrc
        })

    return devices


def detect_os(ip):

    packet = IP(dst=ip) / ICMP()

    reply = sr1(packet, timeout=2, verbose=False)

    if reply:

        ttl = reply.ttl

        if ttl <= 64:
            return "Linux / Mac"

        elif ttl <= 128:
            return "Windows"

        else:
            return "Router"

    return "Unknown"


def fingerprint(devices):

    print("\nDevice Fingerprinting")
    print("----------------------------------")

    for device in devices:

        ip = device["ip"]
        mac = device["mac"]

        try:
            vendor = MacLookup().lookup(mac)
        except:
            vendor = "Unknown"

        os_guess = detect_os(ip)

        print(f"IP: {ip}")
        print(f"MAC: {mac}")
        print(f"Vendor: {vendor}")
        print(f"OS Guess: {os_guess}")
        print()


def main():

    devices = scan_network()

    fingerprint(devices)


if __name__ == "__main__":
    main()
