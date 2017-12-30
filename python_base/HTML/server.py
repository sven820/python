__author__ = "JJ.sven"

import socket
import gevent


def server(addr, port):
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # adress重用

    try:
        s.bind((addr, port))
    except Exception as e:
        print(e)
    else:
        s.listen()
        print('server start listen')
        while True:
            try:
                conn, address = s.accept()
                gevent.spawn(handlerequest, conn)
            except Exception as e:
                print('accept conn error, conn>> ', conn)
                print(e)


    finally:
        s.close()


def handlerequest(conn):
    while True:
        try:
            data = conn.recv(1024)
        except Exception as e:
            data = None
            print('conn recv error', e)
        finally:
            if not data:
                print('conn disconnect')
                conn.close()
                break;
            else:
                conn.send(data.upper())


if __name__ == '__main__':
    server('localhost', 9090)
