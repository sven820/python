__author__ = "JJ.sven"

import gevent
from gevent import monkey
import time
from urllib import request

# 默认gevent检测不到request的IO操作，patch_all会抓取到request的IO操作
monkey.patch_all()

def f(url, filename):

    resp = request.urlopen(url=url)
    data = resp.read()

    file = open(filename, 'wb')
    file.write(data)
    file.close()

    # print(data.decode())

urls = ['https://www.python.org/',
        'https://www.yahoo.com/',
        'https://github.com/' ]
names = ['python',
        'yahoo',
        'github' ]
time_start = time.time()
for index, url in enumerate(urls):
    f(url, names[index])

print('同步time ', time.time() - time_start)

time_start_async = time.time()
gevent.joinall([
    gevent.spawn(f, 'https://www.python.org/', 'python'),
    gevent.spawn(f, 'https://www.yahoo.com/', 'yahoo'),
    gevent.spawn(f, 'https://github.com/', 'github')
])
print('异步time ', time.time() - time_start_async)
