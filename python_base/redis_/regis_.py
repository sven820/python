__author__ = "JJ.sven"

'''redis_ 非关系数据库， 健值对保存数据

支持string， set， hash 。。。

doc http://www.cnblogs.com/alex3714/articles/6217453.html
'''

import redis

r = redis.Redis(host='localhost', port=6379)
r.set('foo', 'Bar')
print(r.get('foo'))
print(r.get('name'))

'''管道'''

pool = redis.ConnectionPool(host='localhost', port=6379)

r1 = redis.Redis(connection_pool=pool)

'''pipline实现一次请求指定多个命令'''
# pipe = r.pipeline(transaction=False)
pipe = r1.pipeline(transaction=True)

pipe.set('name', 'jxf')
pipe.set('age', 18)
pipe.execute()

print(r1.get('name'), '---', r1.get('age'))