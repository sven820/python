# -*- coding:gbk -*-
__author__ = "JJ.sven"

import sys

default = sys.getdefaultencoding()
print(default)

# python2默认编码集是ASCII码， python3默认是unicode

# utf8 格式
'''
s = '你好啊'
s_gbk = s.encode('gbk')
print(s_gbk.decode('gbk'))

gbk_utf8 = s_gbk.decode('gbk').encode('utf-8')
print(gbk_utf8.decode())
'''

# gbk 格式, 记得申明文件编码格式
s = '你好啊' # 这里是unicode的，因为p3是unicode的

s_utf8 = s.encode('utf-8')
print(s_utf8.decode('utf-8'))

s_utf8_gbk = s_utf8.decode('utf-8').encode('gbk')
print(s_utf8_gbk.decode('gbk'))


