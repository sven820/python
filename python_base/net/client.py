__author__ = "JJ.sven"

import socket

client = socket.socket()

res = client.connect(('localhost', 9999))
print(res)
while True:
    content = input('>>: ').strip()
    if len(content) <= 0: continue # 不能发送空内容
    client.send(content.encode())
    print('send: ', content)
    rdata = client.recv(1024)
    print('recv: ', rdata.decode())

client.close()
