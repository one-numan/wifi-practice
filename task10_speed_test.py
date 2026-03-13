"""
task10_speed_test.py

Question 10:
How to measure internet speed using Python?

This script:
1. Connects to nearest speed test server
2. Measures latency (ping)
3. Measures download speed
4. Measures upload speed
"""

import speedtest


def run_speed_test():
    """
    Perform internet speed test.
    """

    print("Finding best server...")

    st = speedtest.Speedtest()

    st.get_best_server()

    print("Running download test...")
    download_speed = st.download()

    print("Running upload test...")
    upload_speed = st.upload()

    ping = st.results.ping

    return {
        "ping": ping,
        "download": download_speed,
        "upload": upload_speed
    }


def convert_to_mbps(speed):
    """
    Convert bits per second to Mbps.
    """

    return round(speed / 1_000_000, 2)


def main():

    result = run_speed_test()

    print("\nInternet Speed Test Result")
    print("----------------------------------")

    print("Ping      :", result["ping"], "ms")
    print("Download  :", convert_to_mbps(result["download"]), "Mbps")
    print("Upload    :", convert_to_mbps(result["upload"]), "Mbps")


if __name__ == "__main__":
    main()
