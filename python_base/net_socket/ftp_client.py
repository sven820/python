__author__ = "JJ.sven"

import socket
import os
import json
import hashlib

'''
1. client
2. client.connect(ip, prot)
3. client.send -|
                |
4. client.recv _|  
5. close
'''

'''
当连续发包时，就可能会粘包
防止粘包要点：
1.分割数据包，不同数据包之间通过ack 消息来分开粘包
2.server 与 client约定task（request）结束的标记,每个task（request）， 都由客户端来ack结束
'''

client = socket.socket()


def simple_send(client):
    content = input('>> ').strip()
    print('send: \n', content)
    client.send(content.encode())

    r_data = client.recv(1024)
    print('recv server data: \n', r_data.decode())


def shellcmd(client):
    content = input('cmd >> ').strip()
    print('send: \n', content)
    client.send(content.encode())

    length = int(client.recv(1024).decode())
    print('recv length is ', length)
    print('client acked length: ', length)
    client.send('client acked length'.encode())

    recv_size = 0
    recv_data = bytes()

    ''' 接受大量数据操作
    防止粘包，最后size根据剩下的取'''
    while recv_size < length:
        if length - recv_size < 1024:
            size = length - recv_size
            print('last recv size: ', size)
        else:
            size = 1024
        data = client.recv(size)
        recv_data += data
        recv_size += len(data)
    print('recv length: ', recv_size)
    print('recv server data: \n', recv_data.decode())


def file_operation(client):
    data = client.recv(1024).decode()
    print(data)
    cmd = input('cmd >> ').strip()
    client.send(cmd.encode())

    cmd_data = cmd.split(' ')
    if cmd_data[0] == 'down':
        file_operation_down(client, cmd)
    elif cmd_data[0] == 'upload':
        if cmd_data.__len__() > 1:
            file_operation_upload(client, cmd, cmd_data[1])
        else:
            file_operation_upload(client, cmd, '')
    else:
        pass


def file_operation_down(client, cmd):

    info = json.loads(client.recv(1024).decode())
    length = int(info['length'])
    name = info['name']
    newname = 'new_' + name

    if length <= 0:
        print(info['info'])
    else:
        print('down file info', info)

        client.send('ack for down file info'.encode())

        recv_size = 0
        recv_data = bytes()
        dmd5 = hashlib.md5()
        while recv_size < length:
            if length - recv_size < 1024:
                size = length - recv_size
            else:
                size = 1024
            data = client.recv(size)
            recv_size += len(data)
            recv_data += data
            dmd5.update(data)

        print('down load done')
        md5 = client.recv(1024).decode()
        if md5 == dmd5.hexdigest():
            f = open(newname, 'wb')
            f.write(recv_data)
            f.close()
        else:
            print('file has been tampered')

    client.send('ack operation over'.encode())
    print('oeration over , new operation please input new cmd')


def file_operation_upload(client, cmd, filename):
    info = {'length': 0, 'info': '', 'name': filename}
    if os.path.isfile(filename):
        file = open(filename, 'rb')
        filesize = os.stat(filename).st_size
        info['length'] = filesize
        client.send(json.dumps(info).encode())

        ack = client.recv(1024).decode() # 收到server确认，准备上传
        print('server ack for upload: ', ack)
        for line in file:
            client.send(line)
        print('upload done')
    else:
        info['info'] = 'error, operation over'
        print(info['info'])
        client.send(json.dumps(info).encode())

    ack = client.recv(1024).decode() # server ack operation done
    print(ack)

    client.send('ack operation over'.encode())
    print('oeration over , new operation please input new cmd')

try:
    client.connect(('localhost', 9898))
except ConnectionRefusedError as e:
    print('server refused')
else:
    while True:
        try:
            # simple_send(client)
            # shellcmd(client)
            file_operation(client)
        except Exception as e:
            print(e)
            raise e
            break
finally:
    client.close()
