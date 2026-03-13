# wifi-practice
A collection of Wi-Fi experiments, tools, and research notes covering wireless networking, protocols, and security.

____


## WiFi & Network Security Toolkit (Python)

A collection of practical Python scripts for **WiFi analysis, network discovery, monitoring, and security research**.

This toolkit demonstrates how common networking and security techniques work internally, including:

* Network scanning
* Device discovery
* Packet sniffing
* DNS monitoring
* Bandwidth analysis
* WiFi signal analysis
* Rogue access point detection
* ARP spoof detection
* Device fingerprinting
* Network topology visualization

The project is structured as **incremental tasks**, where each script focuses on a specific networking concept.

---

# Project Structure

```
wifi-practice/

task01_detect_network.py
task02_scan_active_devices.py
task03_ping_device.py
task04_detect_mac.py
task05_detect_vendor.py
task06_device_inventory.py
task07_detect_router.py
task08_port_scanner.py
task09_packet_sniffer.py
task10_speed_test.py
task11_dns_sniffer.py
task12_connection_monitor.py
task13_dns_analyzer.py
task14_wifi_rssi.py
task15_wifi_distance.py
task16_wifi_movement_tracker.py
task17_deauth_detector.py
task18_wifi_heatmap.py
task19_network_anomaly_detector.py
task20_device_fingerprinting.py
task21_arp_spoof_detector.py
task22_real_network_topology.py
task23_bandwidth_monitor.py
task24_wifi_channel_scanner.py
task25_rogue_ap_detector.py
```

---

# Prerequisites

## Python

Python 3.9 or higher recommended.

```
python3 --version
```

---

## Virtual Environment (Recommended)

Create and activate a virtual environment.

```
python3 -m venv .venv
source .venv/bin/activate
```

---

## Required Python Libraries

Install dependencies:

```
pip install scapy
pip install speedtest-cli
pip install mac-vendor-lookup
pip install pandas
pip install scikit-learn
pip install matplotlib
pip install networkx
pip install numpy
pip install pyobjc
pip install netifaces
```

Optional but useful:

```
pip install python-nmap
```

---

# System Requirements

## Operating System

Best compatibility:

* macOS (for CoreWLAN WiFi scanning)
* Linux (recommended for advanced WiFi analysis)

Some scripts require **root privileges**.

Run using:

```
sudo python3 script_name.py
```

---

# Core Networking Features

## Network Discovery

| Script                        | Description                    |
| ----------------------------- | ------------------------------ |
| task01_detect_network.py      | Detect local network range     |
| task02_scan_active_devices.py | Scan active devices on network |
| task03_ping_device.py         | Check if device is reachable   |
| task04_detect_mac.py          | Detect MAC addresses           |
| task05_detect_vendor.py       | Identify vendor from MAC       |

---

## Device & Network Information

| Script                     | Description               |
| -------------------------- | ------------------------- |
| task06_device_inventory.py | Generate device inventory |
| task07_detect_router.py    | Detect default gateway    |
| task08_port_scanner.py     | Scan open ports on device |

---

## Traffic Monitoring

| Script                       | Description                       |
| ---------------------------- | --------------------------------- |
| task09_packet_sniffer.py     | Capture network packets           |
| task10_speed_test.py         | Measure internet speed            |
| task11_dns_sniffer.py        | Detect DNS requests               |
| task12_connection_monitor.py | Monitor TCP/UDP connections       |
| task13_dns_analyzer.py       | Analyze DNS queries and responses |

---

## WiFi Analysis

| Script                          | Description                          |
| ------------------------------- | ------------------------------------ |
| task14_wifi_rssi.py             | Measure WiFi signal strength         |
| task15_wifi_distance.py         | Estimate distance using RSSI         |
| task16_wifi_movement_tracker.py | Detect device movement               |
| task17_deauth_detector.py       | Detect WiFi deauthentication attacks |
| task18_wifi_heatmap.py          | Generate WiFi signal heatmap         |

---

## Security & Monitoring

| Script                             | Description                |
| ---------------------------------- | -------------------------- |
| task19_network_anomaly_detector.py | AI-based anomaly detection |
| task20_device_fingerprinting.py    | Detect device type and OS  |
| task21_arp_spoof_detector.py       | Detect ARP spoof attacks   |
| task22_real_network_topology.py    | Visualize network topology |
| task23_bandwidth_monitor.py        | Monitor bandwidth usage    |
| task24_wifi_channel_scanner.py     | Scan WiFi channels         |
| task25_rogue_ap_detector.py        | Detect rogue access points |

---

# Example Usage

Run any script using:

```
python3 task08_port_scanner.py
```

Some scripts require elevated privileges:

```
sudo python3 task09_packet_sniffer.py
```

---

# Educational Purpose

This project is designed for:

* Networking students
* Cybersecurity learners
* Python developers interested in networking
* Security research experiments

---

# Important Notes

Some WiFi features are **restricted on macOS** due to system security policies.

Advanced WiFi analysis may require:

* Linux environment
* External WiFi adapter supporting monitor mode

---

# Future Improvements

Potential extensions for this project:

* Real-time monitoring dashboard
* Web interface (FastAPI + React)
* Device behavior analytics
* WiFi intrusion detection
* Real-time traffic visualization

---

# Disclaimer

This toolkit is intended **for educational and research purposes only**.

Do not use these tools on networks without authorization.

Unauthorized network scanning or monitoring may violate laws and regulations.
