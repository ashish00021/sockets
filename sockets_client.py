# sockets client

import socket

# defined the properties of Network : socket.AF_INET is for IPV4 , and socket.SOCK_STREAM is for TCP connection
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client_socket.connect(('127.0.0.1',5090)) # .connect makes connections with server

while True:

    data = input("Enter the data to send : ")
    client_socket.send(data.encode())

    server_data = client_socket.recv(1024)
    if server_data == '': break
    print("[+] Server send ; ", server_data.decode())


client_socket.close()