import socket

target_host = "127.0.0.1"
target_port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #creating socket object

client.sendto("AAABBBCCC", (target_host,target_port))  #sending data

data, addr = client.recvfrom(4096) # reciving data

print data