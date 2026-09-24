import nmap

# Create Nmap scanner
scanner = nmap.PortScanner(
    nmap_search_path=(r"C:\Program Files (x86)\Nmap\nmap.exe",)
)

print("Welcome this is a simple Nmap automation tool")
print("=" * 75)

# MagetoDev Nmap Scanner Banner
print(r"""
███╗   ███╗ █████╗  ██████╗ ███████╗████████╗ ██████╗ ██████╗ ███████╗██╗   ██╗
████╗ ████║██╔══██╗██╔════╝ ██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗██╔════╝██║   ██║
██╔████╔██║███████║██║  ███╗█████╗     ██║   ██║   ██║██║  ██║█████╗  ██║   ██║
██║╚██╔╝██║██╔══██║██║   ██║██╔══╝     ██║   ██║   ██║██║  ██║██╔══╝  ╚██╗ ██╔╝
██║ ╚═╝ ██║██║  ██║╚██████╔╝███████╗   ██║   ╚██████╔╝██████╔╝███████╗ ╚████╔╝
╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝   ╚═════╝ ╚═════╝ ╚══════╝  ╚═══╝

                    M A G E T O D E V
                       Nmap Scanner
""")

print("=" * 75)
print("                 MAGETODEV SECURITY TOOL")
print("=" * 75)

ip_addr = input("Please enter the IP address you want to scan: ")

print("The IP you entered is:", ip_addr)

resp = input("""
Please enter the type of scan you want to run:

1) SYN ACK Scan
2) UDP Scan
3) Comprehensive Scan

Enter your choice: """)

print("You have selected option:", resp)

# SYN ACK Scan
if resp == '1':

    print("\n" + "=" * 75)
    print("                 MAGETODEV SYN ACK SCAN")
    print("=" * 75)

    print("Nmap version:", scanner.nmap_version())
    print(f"Target: {ip_addr}")
    print("Ports: 1-1024")

    print("\n[+] SCAN IN PROGRESS...")
    print("[+] Running SYN ACK scan...")
    print("[+] Please wait...\n")

    scanner.scan(
        ip_addr,
        '1-1024',
        '-v -sS'
    )

    print("\n[+] SCAN COMPLETE!")
    print("=" * 75)

    print("Scan information:", scanner.scaninfo())
    print("IP Status:", scanner[ip_addr].state())
    print("Protocols:", scanner[ip_addr].all_protocols())

    if 'tcp' in scanner[ip_addr]:

        print("\nOpen TCP Ports:")

        for port in scanner[ip_addr]['tcp']:
            state = scanner[ip_addr]['tcp'][port]['state']
            service = scanner[ip_addr]['tcp'][port].get('name', 'unknown')

            print(
                f"Port {port}: {state} | "
                f"Service: {service}"
            )

    else:
        print("No TCP ports found.")

    print("=" * 75)


# UDP Scan
elif resp == '2':

    print("\n" + "=" * 75)
    print("                   MAGETODEV UDP SCAN")
    print("=" * 75)

    print("Nmap version:", scanner.nmap_version())
    print(f"Target: {ip_addr}")
    print("Ports: 1-1024")

    print("\n[+] SCAN IN PROGRESS...")
    print("[+] Running UDP scan...")
    print("[+] Please wait...\n")

    scanner.scan(
        ip_addr,
        '1-1024',
        '-v -sU'
    )

    print("\n[+] SCAN COMPLETE!")
    print("=" * 75)

    print("Scan information:", scanner.scaninfo())
    print("IP Status:", scanner[ip_addr].state())
    print("Protocols:", scanner[ip_addr].all_protocols())

    if 'udp' in scanner[ip_addr]:

        print("\nUDP Ports:")

        for port in scanner[ip_addr]['udp']:
            state = scanner[ip_addr]['udp'][port]['state']
            service = scanner[ip_addr]['udp'][port].get('name', 'unknown')

            print(
                f"Port {port}: {state} | "
                f"Service: {service}"
            )

    else:
        print("No UDP ports found.")

    print("=" * 75)


# Comprehensive Scan
elif resp == '3':

    print("\n" + "=" * 75)
    print("             MAGETODEV COMPREHENSIVE SCAN")
    print("=" * 75)

    print("Nmap version:", scanner.nmap_version())
    print(f"Target: {ip_addr}")
    print("Ports: 1-1024")

    print("\n[+] SCAN IN PROGRESS...")
    print("[+] Running SYN scan...")
    print("[+] Detecting services and versions...")
    print("[+] Performing additional detection...")
    print("[+] Please wait...\n")

    scanner.scan(
        ip_addr,
        '1-1024',
        '-v -sS -sV -A -O'
    )

    print("\n[+] SCAN COMPLETE!")
    print("=" * 75)

    print("Scan information:", scanner.scaninfo())
    print("IP Status:", scanner[ip_addr].state())
    print("Protocols:", scanner[ip_addr].all_protocols())

    if 'tcp' in scanner[ip_addr]:

        print("\nOpen TCP Ports:")

        for port in scanner[ip_addr]['tcp']:

            port_info = scanner[ip_addr]['tcp'][port]

            state = port_info.get('state', 'unknown')
            service = port_info.get('name', 'unknown')
            product = port_info.get('product', '')
            version = port_info.get('version', '')

            print(
                f"Port {port}: {state} | "
                f"Service: {service} | "
                f"Product: {product} | "
                f"Version: {version}"
            )

    else:
        print("No TCP ports found.")

    print("=" * 75)


# Invalid option
else:

    print("\n[!] Invalid option.")
    print("[!] Please enter 1, 2, or 3.")

