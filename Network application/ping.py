import sys
from socket import *
from scapy.all import *
print("pinging target....")

ip = '192.168.2.26'

# command line argument
icmp = IP(dst=ip)/ICMP()

response = sr1(icmp,timeout=10)

#look for a response, if not found the host is not online
if response == None:
    print("This host is not online")
   
else:
    print("This host is online")
