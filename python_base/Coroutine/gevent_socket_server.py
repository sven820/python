__author__ = "JJ.sven"

'''协程实现多并发'''

import socket
import gevent
from gevent import monkey


monkey.patch_all()

recv_lenght = 1024

def server(port):
    s = socket.socket()
    s.bind(('0.0.0.0', port))
    s.listen(500)
    print('server start')
    while True:
        try:
            conn, adds = s.accept()
            # handlerequest(conn)
            gevent.spawn(handlerequest, conn)
            conn.shutdown()

        except Exception as e:
            break
            print(e)

    s.close()


def handlerequest(conn):

    while True:
        try:
            data = conn.recv(recv_lenght)
            print(data.decode())
            if not data:
                conn.shutdown(socket.SHUT_WR)
                break;
            conn.send(data.upper())
        except Exception as e:
            print(e)
            break;

    conn.close()

if __name__ == '__main__':
    server(9000)