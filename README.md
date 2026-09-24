# Network Recon Tools

A collection of Python-based network reconnaissance and scanning tools developed for cybersecurity learning, network analysis, and authorized security testing.

The repository demonstrates practical use of Python, Scapy, Nmap, socket programming, and basic network reconnaissance techniques.

## Tools

| Tool                      | Description                                                                                          |
| ------------------------- | ---------------------------------------------------------------------------------------------------- |
| `bannergrabber.py`        | Connects to a specified host and port to retrieve available service banners.                         |
| `hostdiscovery.py`        | Uses ARP requests to identify active hosts on a local subnet and display their IP and MAC addresses. |
| `nmap_port_scanner.py`    | Performs port and service discovery using Nmap.                                                      |
| `nmap_scanner_linux.py`   | Nmap-based network scanning workflow designed for Linux environments.                                |
| `nmap_scanner_windows.py` | Nmap-based network scanning workflow designed for Windows environments.                              |
| `python_port_scanner.py`  | A Python-based TCP port scanner using socket connections.                                            |

## Technologies

* Python 3
* Scapy
* Nmap
* Python Socket Library
* ARP
* TCP/IP networking
* Windows and Linux

## Requirements

Depending on the tool you are using, you may need:

* Python 3.x
* Scapy
* Nmap
* Npcap on Windows
* Appropriate network permissions

### Install Scapy

```bash
pip install scapy
```

### Nmap

Nmap is required for the Nmap-based tools.

After installing Nmap, verify that it is available from your terminal:

```bash
nmap --version
```

On Windows, Npcap may also be required for packet-based functionality.

## Usage

Clone the repository:

```bash
git clone https://github.com/Magetojob/Network-Recon-Tools.git
```

Enter the repository:

```bash
cd Network-Recon-Tools
```

Run the desired Python script:

```bash
python bannergrabber.py
```

```bash
python hostdiscovery.py
```

```bash
python nmap_port_scanner.py
```

```bash
python python_port_scanner.py


The tools may request information such as an IP address, port, or subnet depending on the script.

### Host Discovery Example

The host discovery tool accepts a subnet range such as:

192.168.1.0/24


It uses ARP to identify hosts that respond on the local network and displays their IP and MAC addresses.

Example output:

IP Address          MAC Address
192.168.1.1         XX:XX:XX:XX:XX:XX
192.168.1.10        XX:XX:XX:XX:XX:XX
192.168.1.15        XX:XX:XX:XX:XX:XX


### Banner Grabber Example

The banner grabber accepts a target IP address and TCP port:

IP: 192.168.1.10
Port: 22


If the service provides a banner, the tool attempts to display the returned information.

## Project Goals

This project was created to strengthen practical understanding of:

* Network reconnaissance
* Host discovery
* Port scanning
* Service enumeration
* Banner grabbing
* TCP/IP networking
* ARP
* Python network programming
* Nmap automation
* Cross-platform security tooling

## Learning Focus

The tools in this repository are intended to demonstrate the underlying concepts involved in network reconnaissance rather than replace established security tools.

Building these utilities from Python provides practical experience with how reconnaissance techniques work at the network and application levels.

## Security & Authorized Use

These tools are intended for **educational purposes, authorized security testing, and systems or networks that you own or have explicit permission to assess**.

Do not use these tools against systems, networks, or services without authorization.

The author is not responsible for misuse of the tools contained in this repository.

## Disclaimer

This repository is a cybersecurity learning project. The code is provided for educational and research purposes and may require additional configuration depending on the operating system and network environment.

## Author

**Job Mageto**

Cybersecurity / IT enthusiast with an interest in network security, reconnaissance, Python automation, and security tooling.

GitHub:

https://github.com/Magetojob

---

 If you find this project useful for learning, consider starring the repository.
