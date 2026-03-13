"""
task22_real_network_topology.py

Real network topology mapper.

This script:
1. Scans the network
2. Detects devices
3. Builds topology graph
"""

from scapy.all import ARP, Ether, srp
import networkx as nx
import matplotlib.pyplot as plt
import netifaces
import ipaddress


def get_network_range():
    """
    Detect current network range automatically.
    """

    gateway = netifaces.gateways()['default'][netifaces.AF_INET]

    interface = gateway[1]

    addresses = netifaces.ifaddresses(interface)

    ip = addresses[netifaces.AF_INET][0]['addr']
    netmask = addresses[netifaces.AF_INET][0]['netmask']

    network = ipaddress.IPv4Network(f"{ip}/{netmask}", strict=False)

    return str(network)


def scan_network(network):

    print("Scanning network:", network)

    arp = ARP(pdst=network)

    ether = Ether(dst="ff:ff:ff:ff:ff:ff")

    packet = ether / arp

    result = srp(packet, timeout=2, verbose=False)[0]

    devices = []

    for sent, received in result:

        devices.append({
            "ip": received.psrc,
            "mac": received.hwsrc
        })

    return devices


def build_topology(devices):

    G = nx.Graph()

    router_ip = devices[0]["ip"]

    G.add_node(router_ip)

    for device in devices[1:]:

        ip = device["ip"]

        G.add_node(ip)

        G.add_edge(router_ip, ip)

    return G


def draw_topology(G):

    pos = nx.spring_layout(G)

    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color="lightgreen",
        node_size=2500,
        font_size=9
    )

    plt.title("Real Network Topology")

    plt.show()


def main():

    network = get_network_range()

    devices = scan_network(network)

    print("\nDevices Detected:")

    for d in devices:

        print(d)

    graph = build_topology(devices)

    draw_topology(graph)


if __name__ == "__main__":
    main()
