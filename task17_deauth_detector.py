"""
task17_deauth_detector.py

Detect WiFi deauthentication packets.
"""

from scapy.all import sniff, Dot11


def detect_deauth(packet):
    """
    Detect deauthentication frames.
    """

    if packet.haslayer(Dot11):

        if packet.type == 0 and packet.subtype == 12:

            src = packet.addr2
            dst = packet.addr1

            print("\n⚠️ Deauthentication Packet Detected")
            print("-----------------------------")
            print("Source :", src)
            print("Target :", dst)


def start_detector():

    print("Starting Deauth Detector...\n")

    sniff(prn=detect_deauth, store=False)


if __name__ == "__main__":
    start_detector()
