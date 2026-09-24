
from scapy.all import ARP, Ether, srp

def discover(subnet_range):
    ether_layer = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_layer = ARP(pdst=subnet_range)
    packet = ether_layer / arp_layer

    answered, unanswered = srp(packet, timeout=2, verbose=False)

    for sent, received in answered:
        print(received.psrc, received.hwsrc)


subnet_range = input("Enter the subnet range (e.g. 192.168.1.0/24): ")

discover(subnet_range)