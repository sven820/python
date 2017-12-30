__author__ = "JJ.sven"

import socket

recv_length = 1024

def client(address,port):
    c = socket.socket()
    c.connect((address, port))
    while True:
        try:
            cotent = input('>> ').strip()
            c.send(cotent.encode())
            data = c.recv(recv_length)
            print(data.decode())
        except Exception as e:
            break
            print(e)


if __name__ == '__main__':
    client('localhost', 9000)