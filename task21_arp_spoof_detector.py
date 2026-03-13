"""
task21_arp_spoof_detector.py

Detect ARP spoofing attacks by monitoring
IP to MAC address changes.
"""

from scapy.all import sniff, ARP

arp_table = {}


def process_packet(packet):

    if packet.haslayer(ARP):

        ip = packet.psrc
        mac = packet.hwsrc

        if ip in arp_table:

            if arp_table[ip] != mac:

                print("\n⚠️ ARP Spoofing Detected!")
                print("----------------------------")
                print("IP Address :", ip)
                print("Old MAC    :", arp_table[ip])
                print("New MAC    :", mac)

        else:

            arp_table[ip] = mac


def start_detector():

    print("Starting ARP Spoofing Detector...\n")

    sniff(filter="arp", prn=process_packet, store=False)


if __name__ == "__main__":
    start_detector()
