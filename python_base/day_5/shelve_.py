__author__ = "JJ.sven"

import shelve

# 以k，v形式持久化数据，任何类型

d = shelve.open('shelve_test')


l = ['jj', 234, '00']
d['data'] = l
d['time'] = '2018 08 25'

# l = d.get('data')
# print(l)


d.close()
