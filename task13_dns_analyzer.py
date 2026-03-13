"""
task13_dns_analyzer.py

DNS Query + DNS Response analyzer.

Detects:
- DNS queries
- DNS responses
- resolved IP addresses
"""

from scapy.all import sniff, DNS, DNSQR, DNSRR, IP


def process_packet(packet):
    """
    Process captured packets and analyze DNS traffic.
    """

    if packet.haslayer(DNS):

        dns = packet[DNS]

        # DNS Query
        if dns.qr == 0 and packet.haslayer(DNSQR):

            domain = packet[DNSQR].qname.decode()

            src_ip = packet[IP].src if packet.haslayer(IP) else "Unknown"

            print("\nDNS Query")
            print("------------------------")
            print("Source IP :", src_ip)
            print("Domain    :", domain)

        # DNS Response
        elif dns.qr == 1 and packet.haslayer(DNSRR):

            domain = packet[DNSQR].qname.decode()

            ip = packet[DNSRR].rdata

            print("\nDNS Response")
            print("------------------------")
            print("Domain :", domain)
            print("IP     :", ip)


def start_dns_analyzer():
    """
    Start DNS traffic monitoring.
    """

    print("Starting DNS Analyzer...\n")

    sniff(filter="port 53", prn=process_packet, store=False)


if __name__ == "__main__":
    start_dns_analyzer()
