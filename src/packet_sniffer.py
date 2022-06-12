from scapy.all import *

def handler(packet):
    print(packet.summary())

if __name__ == "__main__":
    sniff(iface="en0",prn=handler, store=0)
