"""
task14_wifi_rssi.py

Get WiFi SSID and RSSI on macOS using system_profiler.
"""

import subprocess
import re


def get_wifi_info():
    """
    Extract SSID and RSSI from system_profiler output.
    """

    result = subprocess.run(
        ["system_profiler", "SPAirPortDataType"],
        capture_output=True,
        text=True
    )

    output = result.stdout

    ssid_match = re.search(r"Current Network Information:\n\s*(.+):", output)
    rssi_match = re.search(r"Signal / Noise:\s*(-\d+)", output)

    ssid = ssid_match.group(1) if ssid_match else "Unknown"
    rssi = rssi_match.group(1) if rssi_match else "Unknown"

    return ssid, rssi


def main():

    ssid, rssi = get_wifi_info()

    print("WiFi Information")
    print("----------------------------")

    print("SSID :", ssid)
    print("RSSI :", rssi, "dBm")


if __name__ == "__main__":
    main()
