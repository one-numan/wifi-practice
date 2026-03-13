"""
task19_network_anomaly_detector.py

AI-based network anomaly detection.
"""

from scapy.all import sniff, IP, TCP, UDP
import pandas as pd
from sklearn.ensemble import IsolationForest

data = []


def process_packet(packet):

    if packet.haslayer(IP):

        src = packet[IP].src
        dst = packet[IP].dst
        size = len(packet)

        proto = 0

        if packet.haslayer(TCP):
            proto = 6

        elif packet.haslayer(UDP):
            proto = 17

        data.append([size, proto])


def capture_packets():

    print("Capturing packets...")

    sniff(prn=process_packet, count=200)


def detect_anomaly():

    df = pd.DataFrame(data, columns=["size", "protocol"])

    model = IsolationForest(contamination=0.05)

    df["anomaly"] = model.fit_predict(df)

    anomalies = df[df["anomaly"] == -1]

    print("\nAnomalous Packets Detected:")
    print(anomalies)


def main():

    capture_packets()

    detect_anomaly()


if __name__ == "__main__":
    main()
