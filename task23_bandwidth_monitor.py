"""
task23_bandwidth_monitor.py

Real-time bandwidth monitor per device.
"""

from scapy.all import sniff, IP
from collections import defaultdict

bandwidth = defaultdict(int)


def process_packet(packet):
    print(packet)
    if packet.haslayer(IP):

        src = packet[IP].src
        size = len(packet)

        bandwidth[src] += size


def show_usage():

    print("\nBandwidth Usage")
    print("--------------------------")

    for ip, bytes_used in bandwidth.items():

        mb = round(bytes_used / (1024*1024), 2)

        print(f"{ip} → {mb} MB")


def start_monitor():

    print("Starting Bandwidth Monitor...\n")

    sniff(prn=process_packet, store=False)


if __name__ == "__main__":

    try:

        start_monitor()

    except KeyboardInterrupt:

        show_usage()
