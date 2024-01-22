from scapy.all import Ether, IP, sniff, ARP, sr1, ICMP, TCP

my_frame = Ether() / IP()

print(my_frame)
print('-' * 80)
# print(my_frame.show())
# print(my_frame.summary())
print('-' * 80)

packets = sniff(count=10)
for _ in packets:
  num = 0
  print(packets[num].show())
  num += 1

request  = ARP()
print(request)

request2 = sr1(IP(dst='scanme.nmap.org')/ICMP())

if request2:
  print(request2.show())


host = 'scanme.nmap.org'
port_range = 22
src_port = 22
dst_port =  22

response = sr1(IP(dst=host)/TCP(sport=src_port, dport=dst_port, flags='S'), timeout=1, verbose=0)

print(response.show())
