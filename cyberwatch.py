
---

## acyberwatch.py

```python
import csv
import socket
from datetime import datetime

try:
    import nmap
except ImportError:
    print("Missing dependency: python-nmap")
    print("Install it with: pip install python-nmap")
    exit(1)


APPROVED_ASSETS_FILE = "approved_assets.csv"
SCAN_RESULTS_FILE = "scan_results.csv"


def load_approved_assets():
    approved_assets = {}

    try:
        with open(APPROVED_ASSETS_FILE, mode="r", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                mac = row["mac_address"].strip().lower()
                approved_assets[mac] = {
                    "asset_name": row["asset_name"],
                    "owner": row["owner"],
                    "status": row["status"]
                }

    except FileNotFoundError:
        print(f"Error: {APPROVED_ASSETS_FILE} not found.")
        print("Create the approved_assets.csv file before running the scan.")
        exit(1)

    return approved_assets


def get_hostname(ip_address):
    try:
        hostname = socket.gethostbyaddr(ip_address)[0]
    except socket.herror:
        hostname = "unknown"

    return hostname


def scan_network(subnet):
    scanner = nmap.PortScanner()

    print(f"\nScanning subnet: {subnet}")
    print("This may take a moment...\n")

    scanner.scan(hosts=subnet, arguments="-sn")

    discovered_devices = []

    for host in scanner.all_hosts():
        ip_address = host
        hostname = get_hostname(ip_address)

        mac_address = "unknown"

        if "mac" in scanner[host]["addresses"]:
            mac_address = scanner[host]["addresses"]["mac"].lower()

        discovered_devices.append({
            "ip_address": ip_address,
            "mac_address": mac_address,
            "hostname": hostname
        })

    return discovered_devices


def analyze_devices(discovered_devices, approved_assets):
    scan_results = []

    for device in discovered_devices:
        mac = device["mac_address"].lower()

        if mac in approved_assets:
            asset_info = approved_assets[mac]
            device_status = "Approved"
            asset_name = asset_info["asset_name"]
            owner = asset_info["owner"]
        else:
            device_status = "Unknown"
            asset_name = "Unknown"
            owner = "Unknown"

        result = {
            "scan_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "ip_address": device["ip_address"],
            "mac_address": device["mac_address"],
            "hostname": device["hostname"],
            "asset_name": asset_name,
            "owner": owner,
            "device_status": device_status
        }

        scan_results.append(result)

    return scan_results


def save_results(scan_results):
    fieldnames = [
        "scan_time",
        "ip_address",
        "mac_address",
        "hostname",
        "asset_name",
        "owner",
        "device_status"
    ]

    with open(SCAN_RESULTS_FILE, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(scan_results)

    print(f"\nScan results saved to {SCAN_RESULTS_FILE}")


def display_results(scan_results):
    print("Scan Results")
    print("-" * 80)

    for result in scan_results:
        print(f"IP Address:    {result['ip_address']}")
        print(f"MAC Address:   {result['mac_address']}")
        print(f"Hostname:      {result['hostname']}")
        print(f"Asset Name:    {result['asset_name']}")
        print(f"Owner:         {result['owner']}")
        print(f"Status:        {result['device_status']}")

        if result["device_status"] == "Unknown":
            print("Alert:         UNKNOWN DEVICE DETECTED")

        print("-" * 80)


def main():
    print("CyberWatch")
    print("Lightweight IT Asset Management Scanner")
    print("-" * 80)

    approved_assets = load_approved_assets()

    subnet = input("Enter subnet to scan, example 192.168.1.0/24: ").strip()

    if not subnet:
        print("No subnet entered. Exiting.")
        return

    discovered_devices = scan_network(subnet)
    scan_results = analyze_devices(discovered_devices, approved_assets)

    display_results(scan_results)
    save_results(scan_results)


if __name__ == "__main__":
    main()
