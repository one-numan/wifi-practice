"""
task08_port_scanner.py

Question 8:
How to detect open ports on a device using Python?

This script:
1. Detects router IP automatically
2. Scans common ports
3. Prints open ports and services
"""

import socket
from utils.network_utils import get_router_ip


def scan_port(ip: str, port: int):
    """
    Scan a single port.

    Parameters
    ----------
    ip : str
        Target device IP address
    port : int
        Port number

    Returns
    -------
    tuple | None
        (port, service_name) if open
    """

    try:

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        sock.settimeout(1)

        result = sock.connect_ex((ip, port))

        if result == 0:

            try:
                service = socket.getservbyport(port)
            except:
                service = "Unknown"

            return (port, service)

        sock.close()

    except:
        pass

    return None


def port_scan(ip: str, ports: list):
    """
    Scan multiple ports.
    """

    open_ports = []

    for port in ports:

        result = scan_port(ip, port)

        if result:
            open_ports.append(result)

    return open_ports


def main():

    target_ip = get_router_ip()

    print("Target IP :", target_ip)
    print("-----------------------------")

    ports_to_scan = [
        21, 22, 23, 25,
        53, 80, 110,
        139, 143, 443,
        445, 3389
    ]

    open_ports = port_scan(target_ip, ports_to_scan)

    print("\nOpen Ports")
    print("-----------------------------")

    for port, service in open_ports:

        print(f"{port:<6} {service}")


if __name__ == "__main__":
    main()
