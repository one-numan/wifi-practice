import psutil
from tabulate import tabulate

rows = []

for conn in psutil.net_connections():
    if conn.laddr:

        ip = conn.laddr.ip
        port = conn.laddr.port
        status = conn.status
        pid = conn.pid

        process = "unknown"

        if pid:
            try:
                process = psutil.Process(pid).name()
            except:
                process = "access-denied"

        rows.append([ip, port, status, process, pid])

print("\nACTIVE PORT CONNECTIONS\n")
print(tabulate(rows, headers=["IP", "PORT", "STATUS", "PROCESS", "PID"], tablefmt="grid"))

# summary
total = len(rows)
unique_ports = len(set([r[1] for r in rows]))

print("\nSUMMARY\n")
summary = [
    ["Total connections", total],
    ["Unique ports", unique_ports]
]

print(tabulate(summary, tablefmt="grid"))