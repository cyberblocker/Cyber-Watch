# Cyber Watch

Cyber Watch is a lightweight IT asset management project designed to improve visibility into devices connected to a local network.

The tool scans a user-defined subnet, collects basic device information, compares discovered MAC addresses against an approved asset inventory, and flags unknown devices for review.

## Features

- Scan a local subnet for active devices
- Collect IP addresses, MAC addresses, and hostnames
- Compare discovered devices against an approved asset list
- Detect and flag unknown devices
- Save scan results to a CSV file
- Simple command-line interface

## Why This Project Matters

Asset visibility is a major part of IT operations and cybersecurity. Organizations need to know what devices are connected to their network, which systems are approved, and when unknown devices appear.

This project demonstrates practical skills in:

- IT asset management
- Network discovery
- Python scripting
- Basic security monitoring
- Inventory tracking
- CSV-based reporting

## Example Use Case

An IT technician runs AssetWatch on a local network. The tool discovers several devices and checks them against the approved asset list.

If a new or unauthorized device appears, AssetWatch flags it as unknown.

Example alert:

```text
[UNKNOWN DEVICE DETECTED]
IP Address: 192.168.1.45
MAC Address: AA:BB:CC:DD:EE:FF
Hostname: unknown
Status: Review Required
```

## Requirements

- Python 3
- Nmap installed on your system
- python-nmap library

Install the Python dependency:

pip install python-nmap

Install Nmap:

sudo apt install nmap

For Windows, download Nmap from the official Nmap website and make sure it is added to your system PATH.

approved_assets.csv Format

Create a file named approved_assets.csv:

asset_name,mac_address,owner,status
Cyber-Laptop,AA:BB:CC:DD:EE:11,Cyber,Approved
Home-Router,AA:BB:CC:DD:EE:22,Cyber,Approved
Lab-VM,AA:BB:CC:DD:EE:33,Cyber,Approved

## How to Run

python cyberwatch.py

When prompted, enter a subnet:

Enter subnet to scan: 192.168.1.0/24

Output

AssetWatch will display discovered devices and identify whether they are approved or unknown.

It will also save results to:

scan_results.csv

## Disclaimer

This tool is intended for educational use and should only be used on networks you own or have permission to scan.
