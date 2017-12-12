__author__ = "JJ.sven"

import socketserver
import os
import json
import hashlib

'''socketserver 支持多client操作，每个客户端连进来就会开个线程
    
   具体数据应答操作全部在handle里自己写
'''


class MyHandle(socketserver.BaseRequestHandler):

    def simpleText(self):
        while True:
            try:
                self.data = self.request.recv(1024)
                print('recv data: ', self.data.decode())
                if self.data:
                    self.request.send(self.data.decode().upper().encode())
                else:
                    print('client disconnect')
                    break
            except Exception as e:
                print('error: ', e)
                break

    def file_operation(self):
        while True:
            sources = '''
                opertaion   :
                            - down filename
                            - upload filename
                source files: 
                            - tcp_flow.png 
                            - tcp_osi.png
                '''
            self.request.send(sources.encode())
            cmd = self.request.recv(1024).decode()
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

                    self.request.send(json.dumps(info).encode())
                    ack = self.request.recv(1024)  # wait ack for send file data

                    for line in file:
                        md5.update(line)
                        self.request.send(line)

                    print('file md5', md5.hexdigest())
                    file.close()
                    self.request.send(md5.hexdigest().encode())  # send md5

                else:
                    info['info'] = 'operation error'
                    self.request.send(json.dumps(info).encode())

                ack = self.request.recv(1024)  # 确认文件传输完毕
                print(ack.decode())
                print('send done')

            elif cmd_data[0] == 'upload':
                info = json.loads(self.request.recv(1024).decode())
                filename = info['name']
                newname = 'new_' + filename
                filesize = int(info['length'])
                if filesize > 0:
                    self.request.send('ack for upload info'.encode())

                    recv_size = 0
                    recv_data = bytes()
                    while recv_size < filesize:
                        if filesize - recv_size < 1024:
                            size = filesize - recv_size
                        else:
                            size = 1024
                        data = self.request.recv(size)
                        recv_data += data
                        recv_size += len(data)

                    print('upload done')
                    file = open(newname, 'wb')
                    file.write(recv_data)
                    file.close()

                else:
                    print(info['info'])

                print('upload done')
                self.request.send('server ack upload done'.encode())

                acv_over = self.request.recv(1024).decode()
                print(acv_over)
            else:
                pass

    def handle(self):
        print('client conn in')
        # self.simpleText()
        self.file_operation()

    def setup(self):
        pass
    def finish(self):
        pass

HOST, PORT = 'localhost', 9898
try:
    server = socketserver.ThreadingTCPServer((HOST, PORT), MyHandle)
    server.serve_forever()
    # server.handle_request() server once
except Exception as e:
    print('error: ', e)

print('start server >>')

