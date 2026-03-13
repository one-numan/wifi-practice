"""
task09_packet_sniffer.py

Question 9:
How to monitor network traffic using Python?

This script captures live network packets and prints:
- source IP
- destination IP
- protocol
"""

from scapy.all import sniff, IP


def process_packet(packet):
    """
    Process captured packets.

    Parameters
    ----------
    packet : scapy packet
    """

    if packet.haslayer(IP):

        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = packet[IP].proto

        print("Packet Captured")
        print("-----------------------------")
        print("Source IP      :", src_ip)
        print("Destination IP :", dst_ip)
        print("Protocol       :", protocol)
        print()


def start_sniffer():
    """
    Start network packet capture.
    """

    print("Starting packet sniffer...\n")

    sniff(prn=process_packet, store=False)


if __name__ == "__main__":
    start_sniffer()
