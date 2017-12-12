__author__ = "JJ.sven"

import socket
import os
import hashlib
import json

'''
1. server
2. server.bind(ip, port)
3. server.listen
4. server.accpet() -> conn, addr
5. conn.recv -
              |  
6. conn.send -
7. server.close
'''

server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #adress重用

def simple_send(conn):
    r_data = conn.recv(1024)
    print('recv data: \n', r_data.decode())

    send_data = 'receive data: \n'.encode() + r_data
    print(send_data.decode())
    conn.send(send_data)

def shellcmd(conn):

    r_data = conn.recv(1024).decode()
    print('recv data: \n', r_data)

    send_data = os.popen(r_data).read()
    send_data = 'cmd res empty' if not send_data else send_data
    send_data_encode = send_data.encode()
    send_data_len = len(send_data_encode)

    '''告诉客户端发送数据的长度，让客户端循环接受
       为了让长度信息与后面要发的信息不粘包，客户端发个确认length的信息，server
       收到确认后再发信息
    '''
    print('send length: ', send_data_len)
    conn.send(str(send_data_len).encode())
    ack = conn.recv(1024)
    print('recv client ack length: ', ack.decode())

    print('send: \n', send_data)
    conn.send(send_data_encode)

def file_operation(conn):
    sources = '''
    opertaion   :
                - down filename
                - upload filename
    source files: 
                - tcp_flow.png 
                - tcp_osi.png
    '''
    conn.send(sources.encode())
    cmd = conn.recv(1024).decode()
    cmd_data = cmd.split(' ')
    # print(cmd_data)

    info = {'length': 0, 'info': '', 'name': ''}
    if cmd_data[0] == 'down':
        if len(cmd_data) > 1:
            filename = cmd_data[1]
        else:
            filename = ''
        info['name'] = filename
        if os.path.isfile(filename):
            filesize = os.stat(filename).st_size
            info['length'] = filesize

            file = open(filename, 'rb')
            md5 = hashlib.md5()

            conn.send(json.dumps(info).encode())
            ack = conn.recv(1024) # wait ack for send file data

            for line in file:
                md5.update(line)
                conn.send(line)

            print('file md5', md5.hexdigest())
            file.close()
            conn.send(md5.hexdigest().encode()) # send md5

        else:
            info['info'] = 'operation error'
            conn.send(json.dumps(info).encode())

        ack = conn.recv(1024) #确认文件传输完毕
        print(ack.decode())
        print('send done')

    elif cmd_data[0] == 'upload':
        info = json.loads(conn.recv(1024).decode())
        filename = info['name']
        newname = 'new_' + filename
        filesize = int(info['length'])
        if filesize > 0:
            conn.send('ack for upload info'.encode())

            recv_size = 0
            recv_data = bytes()
            while recv_size < filesize:
                if filesize - recv_size < 1024:
                    size = filesize - recv_size
                else:
                    size = 1024
                data = conn.recv(size)
                recv_data += data
                recv_size += len(data)

            print('upload done')
            file = open(newname, 'wb')
            file.write(recv_data)
            file.close()

        else:
            print(info['info'])

        print('upload done')
        conn.send('server ack upload done'.encode())

        acv_over = conn.recv(1024).decode()
        print(acv_over)
    else:
        pass
try:
    server.bind(('localhost', 9898))
    # socket.bind(('0.0.0.0', 9898))
    server.listen(5)
    print('start listeing:')
except Exception as e:
    print(e)
else:
    while True:
        conn, addr = server.accept()
        print('addr: ', addr, '\n',
              'conn: ', conn)
        while True:
            try:
                # simple_send(conn)
                # shellcmd(conn)
                file_operation(conn)
            except Exception as e:
                print(e)
                break

finally:
    server.close()
