"""
task12_connection_monitor.py

Question 12:
Monitor TCP/UDP connections in network traffic.

This script captures packets and prints:
- source IP
- source port
- destination IP
- destination port
- protocol
"""

from scapy.all import sniff, IP, TCP, UDP


def process_packet(packet):
    """
    Process captured packet and extract connection information.
    """

    if packet.haslayer(IP):

        src_ip = packet[IP].src
        dst_ip = packet[IP].dst

        if packet.haslayer(TCP):

            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport

            print("\nTCP Connection")
            print("-------------------------")
            print(f"{src_ip}:{src_port} → {dst_ip}:{dst_port}")

        elif packet.haslayer(UDP):

            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport

            print("\nUDP Packet")
            print("-------------------------")
            print(f"{src_ip}:{src_port} → {dst_ip}:{dst_port}")


def start_monitor():
    """
    Start monitoring network connections.
    """

    print("Starting connection monitor...\n")

    sniff(prn=process_packet, store=False)


if __name__ == "__main__":
    start_monitor()
