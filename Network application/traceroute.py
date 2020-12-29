from scapy.all import *
host = "192.168.2.26"
for i in range(1, 28):
    packet = IP(dst=host, ttl=i) / UDP(dport=33434)
    # Send the packet and get a reply
    target = sr1(packet, verbose=0)
    #nothing is found
    if target is None:
        break
    #the target was reached
    elif target.type == 3:
        print ("Target reached", target.src)
        break
    #otherwise just loop through until you reach the target
    else:
        print ("%d hops away - " %i , target.src)
