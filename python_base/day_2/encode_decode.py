# -*- coding:gbk -*-
__author__ = "JJ.sven"

import sys

default = sys.getdefaultencoding()
print(default)

# python2Ĭ�ϱ��뼯��ASCII�룬 python3Ĭ����unicode

# utf8 ��ʽ
'''
s = '��ð�'
s_gbk = s.encode('gbk')
print(s_gbk.decode('gbk'))

gbk_utf8 = s_gbk.decode('gbk').encode('utf-8')
print(gbk_utf8.decode())
'''

# gbk ��ʽ, �ǵ������ļ������ʽ
s = '��ð�' # ������unicode�ģ���Ϊp3��unicode��

s_utf8 = s.encode('utf-8')
print(s_utf8.decode('utf-8'))

s_utf8_gbk = s_utf8.decode('utf-8').encode('gbk')
print(s_utf8_gbk.decode('gbk'))


