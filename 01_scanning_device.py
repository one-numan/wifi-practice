import nmap

# create scanner
scanner = nmap.PortScanner()

# network range
network = "10.42.58.0/24"

print("Scanning network:", network)
print("-----------------------------")

# scan
scanner.scan(hosts=network, arguments="-sn")

# show results
for host in scanner.all_hosts():
    print("Device IP:", host)