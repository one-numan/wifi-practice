"""
all_running_port.py

Advanced network connection monitor.

This script lists active network connections on the system and provides
detailed information including:

- Protocol (TCP / UDP)
- Local IP and Port
- Remote IP and Port
- Connection status
- Process name
- Process ID

It also generates a summary of:
- Total connections
- Unique ports
- Unique remote hosts

Libraries:
- psutil: system and network inspection
- tabulate: formatted table output
"""

import psutil
from tabulate import tabulate

rows = []

for conn in psutil.net_connections():

    # Detect protocol
    protocol = "TCP"
    if conn.type == psutil.SOCK_DGRAM:
        protocol = "UDP"

    # Local address
    local_ip = ""
    local_port = ""

    if conn.laddr:
        local_ip = conn.laddr.ip
        local_port = conn.laddr.port

    # Remote address
    remote_ip = ""
    remote_port = ""

    if conn.raddr:
        remote_ip = conn.raddr.ip
        remote_port = conn.raddr.port

    status = conn.status
    pid = conn.pid

    process = "unknown"

    if pid:
        try:
            process = psutil.Process(pid).name()
        except:
            process = "access-denied"

    # Detect connection direction
    direction = "local"

    if remote_ip:
        if status == "LISTEN":
            direction = "incoming"
        else:
            direction = "outgoing"

    rows.append([
        protocol,
        local_ip,
        local_port,
        remote_ip,
        remote_port,
        status,
        direction,
        process,
        pid
    ])

print("\nACTIVE NETWORK CONNECTIONS\n")

print(tabulate(
    rows,
    headers=[
        "PROTO",
        "LOCAL IP",
        "LOCAL PORT",
        "REMOTE IP",
        "REMOTE PORT",
        "STATUS",
        "DIRECTION",
        "PROCESS",
        "PID"
    ],
    tablefmt="grid"
))

# -------------------------
# Summary Section
# -------------------------

total = len(rows)

unique_ports = len(set([r[2] for r in rows if r[2]]))

unique_hosts = len(set([r[3] for r in rows if r[3]]))

summary = [
    ["Total connections", total],
    ["Unique local ports", unique_ports],
    ["Unique remote hosts", unique_hosts]
]

print("\nSUMMARY\n")
print(tabulate(summary, tablefmt="grid"))
