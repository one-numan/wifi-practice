"""
task11_dns_sniffer.py

Question 11:
How to detect DNS queries using Python?

This script captures DNS requests and prints
the domain name being queried.
"""
from scapy.all import sniff, DNSQR, IP


def process_packet(packet):
    """
    Process packet and extract DNS query.
    """

    # Check DNS query layer
    if packet.haslayer(DNSQR):

        domain = packet[DNSQR].qname.decode()

        # Check IP layer before accessing
        if packet.haslayer(IP):
            src_ip = packet[IP].src
        else:
            src_ip = "Unknown"

        print("\nDNS Query Detected")
        print("------------------------")
        print("Source IP :", src_ip)
        print("Domain    :", domain)


def start_sniffer():

    print("Starting DNS sniffer...\n")

    sniff(filter="udp port 53", prn=process_packet, store=False)


if __name__ == "__main__":
    start_sniffer()