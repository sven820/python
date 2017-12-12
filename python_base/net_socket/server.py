__author__ = "JJ.sven"

import socket
import os

server = socket.socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #adress重用

server.bind(('localhost', 9898))
# server.bind(('0.0.0.0', 9898)) # 0.0.0.0表示所有网卡的ip地址
server.listen(1)  # 最大允许链接数5

print('开始监听端口')

while True:
    conn, addr = server.accept() #监听的客户端进来
    print('client come in \n', conn, addr)

    while True:
        data = conn.recv(1024).decode() # 1024字节,阻塞在这，直到客户端发来数据
        if not data:
            print('client has lost')
            break
        else:
            # print('client data: ', data)
            # conn.send(data.upper().encode())
            # 循环全部发送掉数据
            # conn.sendall(data.upper().encode())

            # 实现shell cmd操作
            print('receive cmd: ', data)
            cmd_res = os.popen(data).read()
            if not cmd_res:
                cmd_res = 'res empty'

            send_d = cmd_res.encode()
            # 告诉客户端要发送的大小，客户端根据这个大小来决定接受多少次数据
            conn.send(str(len(send_d)).encode())
            # 为解决粘包问题（连续两次send，socket可能会将两次数据当成一条一起发送）
            ack = conn.recv(1024)
            print('receive ack send length ', ack.decode())
            conn.send(send_d)
            print('send done')

server.close()
