__author__ = "JJ.sven"

import select
import socket
import queue

'''
在python中，select函数是一个对底层操作系统的直接访问的接口。它用来监控sockets、files和pipes，
等待IO完成(Waiting for I/O completion)。当有可读、可写或是异常事件产生时，select可以很容易的监控到。
'''
'''
处理思想
select要监控IO的为3类，分3个队列 input output error, 

1 input如果有IO返回，则轮询将input conn计入output，同时起一个queue来保存data
2 下个轮询里，轮询output，处理data
3 如果conn error，则在error轮询里处理相关逻辑
'''

'''
select的一个缺点在于单个进程能够监视的文件描述符的数量存在最大限制，在Linux上一般为1024，
不过可以通过修改宏定义甚至重新编译内核的方式提升这一限制。

另外，select()所维护的存储大量文件描述符的数据结构，随着文件描述符数量的增大，其复制的开销也线性增长。
同时，由于网络响应时间的延迟使得大量TCP连接处于非活跃状态，但调用select()会对所有socket进行一次线性扫描，
所以这也浪费了一定的开销
'''

inputs = []
outputs = []
message_queue = {} # {conn: dataqueue}
recv_length = 1024

def select_server(ip, port):

    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # adress重用
    server.setblocking(False)

    inputs.append(server)
    try:
        server.bind((ip, port))
    except Exception as e:
        print(e)
    else:
        server_listen(server)
    finally:
        server.close()

def server_listen(server):
    server.listen(100000)
    print('server start listenning')

    while True:
        readable, writeable, exceptional = select.select(inputs, outputs, inputs)

        '''inputs'''
        for item in readable:
            if item is server:
                conn, addr = server.accept()
                print('did accept conn: ', addr)
                # 为了不阻塞整个程序,我们不会立刻在这里开始接收客户端发来的数据, 把它放到inputs里, 下一次loop时,这个新连接
                # 就会被交给select去监听,如果这个连接的客户端发来了数据 ,那这个连接的fd在server端就会变成就续的,select就会把这个连接返回,返回到
                # readable 列表里,然后你就可以loop readable列表,取出这个连接,开始接收数据了, 下面就是这么干 的
                conn.setblocking(False)
                inputs.append(conn)
                message_queue[conn] = queue.Queue()
            else:
                try:
                    data = item.recv(recv_length)
                except Exception as e:
                    print(e)
                finally:
                    if data:
                        print('recv conn data: ', data.decode())
                        message_queue[item].put(data)
                        if item not in outputs:
                            outputs.append(item)
                    else:
                        print('conn disconnect')
                        if item in outputs:
                            outputs.remove(item)
                        inputs.remove(item)
                        del message_queue[item]
        for item in writeable:
            try:
                data = message_queue[item].get_nowait()
            except queue.Empty as e:
                print('client[%s] data queue is empty adn remove output conn' % item.getpeername()[0])
                outputs.remove(item)
            else:
                print('send msg to client[%s]' % item.getpeername()[0])
                item.send(data.upper())

        for item in exceptional:
            print('client[%s] exception: ' % item.getpeername()[0])
            inputs.remove(item)
            if item in outputs:
                outputs.remove(item)
            del message_queue[item]
            item.close()




if __name__ == '__main__':
    select_server('localhost', 9000)