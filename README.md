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
