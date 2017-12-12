__author__ = "JJ.sven"

import socket

client = socket.socket()

client.connect(('localhost', 9898))

while True:
    # send
    try:
        content = input('>>: ').strip()
        if len(content) <= 0: continue # 不能发送空内容
        client.send(content.encode())
        print('send: ', content)

        # receive
        length = client.recv(1024).decode()
        print('need receive size is: ', length)
        # 回复server 确认length，防止粘包
        print('ack for data length')
        client.send('confim data length'.encode())

        if length:
            receive_size = 0
            r_data = bytes()
            while receive_size < int(length):
                data = client.recv(1024) # <8192
                r_data += data
                receive_size += len(data)

        print('recv done, size:%s: \n\n' % (receive_size), r_data.decode())
    except BrokenPipeError as e:
        print(e)
    except Exception as e:
        print(e)


client.close()
