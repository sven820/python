__author__ = "JJ.sven"

import socket

server = socket.socket()

server.bind(('localhost', 9999))
server.listen(1)  # 最大允许链接数5

print('开始监听端口')

while True:
    conn, addr = server.accept() #监听的客户端进来
    print('client come in \n', conn, addr)

    while True:
        data = conn.recv(1024).decode()
        if not data:
            print('client has lost')
            break
        else:
            print('client data: ', data)
            conn.send(data.upper().encode())
            # 循环全部发送掉数据
            # conn.sendall(data.upper().encode())

server.close()
