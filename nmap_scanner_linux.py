import nmap

#nm = nmap.PortScanner(
    #nmap_search_path=(r"C:\Program Files (x86)\Nmap\nmap.exe",)
#)
nm = nmap.PortScanner(...)

print("Welcome this is a simple nmap automation tool")
print("=" * 75)


# MagetoDev nmap Scanner Banner

print(r"""
███╗   ███╗ █████╗  ██████╗ ███████╗████████╗ ██████╗ ██████╗ ███████╗██╗   ██╗
████╗ ████║██╔══██╗██╔════╝ ██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗██╔════╝██║   ██║
██╔████╔██║███████║██║  ███╗█████╗     ██║   ██║   ██║██║  ██║█████╗  ██║   ██║
██║╚██╔╝██║██╔══██║██║   ██║██╔══╝     ██║   ██║   ██║██║  ██║██╔══╝  ╚██╗ ██╔╝
██║ ╚═╝ ██║██║  ██║╚██████╔╝███████╗   ██║   ╚██████╔╝██████╔╝███████╗ ╚████╔╝ 
╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝    ╚═════╝ ╚═════╝ ╚══════╝  ╚═══╝  

                    M A G E T O D E V
                      Nmap Scanner
""")

print("=" * 75)
print("                    MAGETODEV SECURITY TOOL")
print("=" * 75)


ip_addr = input("Please enter the IP addresss you want to scan:")
print("The IP you entered is: ", ip_addr)
type(ip_addr)

resp = input("""\nPlease enter the type of scan you want to run
                1)SYN ACK Scan
                2)UDP Scan
                3)Comprehensive Scan\n""")
print("You have selected option: ", resp)

if resp == '1':
    print("Nmap version: ", scanner.nmap_version)
    scanner.scan(ip_addr, '1-1024', '-v -sS')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
elif resp == '2':
    print("Nmap version: ", scanner.nmap_version)
        scanner.scan(ip_addr, '1-1024', '-v -sU')
        print(scanner.scaninfo())
        print("Ip Status: ", scanner[ip_addr].state())
        print(scanner[ip_addr].all_protocols())
        print("Open Ports: ", scanner[ip_addr]['udp'].keys())
elif resp == '3':
    print("Nmap version: ", scanner.nmap_version)
        scanner.scan(ip_addr, '1-1024', '-v -sS -sV -A -O')
        print(scanner.scaninfo())
        print("Ip Status: ", scanner[ip_addr].state())
        print(scanner[ip_addr].all_protocols())
        print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
elif resp >= '4':
    print("Please enter a valid option")