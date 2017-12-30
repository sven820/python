__author__ = "JJ.sven"

# 封装了多路复用（IO multiplexing）的用法，默认使用epoll
import selectors

'''IO操作种类   http://www.cnblogs.com/alex3714/articles/5876749.html

IO 是数据从操作系统内核空间与用户程序的用户空间的数据交换过程

1 blocking IO
2 non blocking IO
3 multi blocking IO （多路复用（IO multiplexing），就是单线程管理并发IO操作，实际还是block的，类似协程
                      采用轮询来判断某个IO操作是否可执行了）
                      
4 async IO 异步IO，真正非阻塞 =》python3支持
'''

'''
目前主流是使用多路复用IO ==》 IO multiplexing
主要操作模式有3种
1 select
    有最大文件描述符数量, linux 一般为1024
    select 函数监视的文件描述符分3类，分别是writefds、readfds、和exceptfds。
    调用后select函数会阻塞，直到有描述副就绪（有数据 可读、可写、或者有except），
    或者超时（timeout指定等待时间，如果立即返回设为null即可），函数返回。
    当select函数返回后，可以 通过遍历fdset，来找到就绪的描述符。

2 poll
    继承自select, poll没有最大文件描述符数量
3 epoll
    是之前的select和poll的增强版本
'''