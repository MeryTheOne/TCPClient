import socket

target_host = "www.google.com"
target_port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creating socket object

client.connect((target_host,target_port)) # connect to klient

client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")  #sending data

response  = client.recvfrom(4096) # reciving data

print response