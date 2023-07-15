# sockets sever

import socket

# defined the properties of Network : socket.AF_INET is for IPV4 , and socket.SOCK_STREAM is for TCP connection
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server_socket.bind(('127.0.0.1',5090)) # given the server adders

server_socket.listen(10)
print("[+] Listening for connections on 127.0.0.1:5090")

while True: # for all client

    conn , addr = server_socket.accept()
    # .accept() use to accept the client request and its return two values :
    # remote connection and client addr
    print("[+] Got a connections from {}".format(addr))


    while True: # for one client

        client_data = conn.recv(1024)
        if client_data == '': break   # for break the loop
        # with conn.recv we get the data of client and 1024 bit is the max value of data we can receive
        print("[+] Client sent:", client_data.decode())

        data = input("Enter the data to send : ")
        conn.send(data.encode())
        # send use to send the data to client in bit b convert string into bit

    conn.close()
