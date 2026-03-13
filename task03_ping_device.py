"""
task03_ping_device.py

Question 3:
How to check if a device is online by pinging an IP address using Python?

This script:
1. Takes an IP address
2. Sends a ping request
3. Detects if the device is online or offline
4. Extracts latency (response time)
"""

import subprocess
import re


def ping_device(ip_address: str) -> dict:
    """
    Ping a device and return its status.

    Parameters
    ----------
    ip_address : str
        Target device IP address.

    Returns
    -------
    dict
        Contains:
        - ip
        - status (online/offline)
        - latency (ms if available)
    """

    try:
        # Send 1 ping request
        result = subprocess.run(
            ["ping", "-c", "1", ip_address],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        output = result.stdout

        if result.returncode == 0:

            latency_match = re.search(r"time=(\d+\.?\d*)", output)

            latency = latency_match.group(1) if latency_match else "Unknown"

            return {
                "ip": ip_address,
                "status": "Online",
                "latency": latency
            }

        else:
            return {
                "ip": ip_address,
                "status": "Offline",
                "latency": None
            }

    except Exception as e:
        return {
            "ip": ip_address,
            "status": "Error",
            "latency": None
        }


def main():
    """
    Main function for testing ping.
    """

    ip = "8.8.8.8"

    result = ping_device(ip)

    print("Ping Result")
    print("----------------------")

    print("IP Address :", result["ip"])
    print("Status     :", result["status"])
    print("Latency    :", result["latency"], "ms")


if __name__ == "__main__":
    main()