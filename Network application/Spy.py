from scapy.all import ARP, Ether, srp

Target = '192.168.2.26'

arp = ARP(pdst=Target) #Arp packet is created

#Stacking the eithers
ether = Ether(dst="ff:ff:ff:ff:ff:ff")

Pkt = ether/arp

#collecting the result
res = srp(Pkt, timeout=3, verbose=0)[0]

c = []  #the list of available clients

for sent, received in res:
    
    c.append({'ip': received.psrc, 'mac': received.hwsrc}) # if the reponse sent it opened the IP and MAC addresses are added to clients.

# print clients
print("The following are the devices on the network:")
print("IP Address" + " "*18+"MAC Address")
for client in c:
    print("{:16}    {}".format(client['ip'], client['mac']))
#end
