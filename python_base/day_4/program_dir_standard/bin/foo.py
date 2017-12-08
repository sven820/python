__author__ = "JJ.sven"

import os
import sys

'''
# 文件的相对路径
print(__file__)
# 文件的绝对路径
print(os.path.abspath(__file__))

# 文件所在目录
print(os.path.dirname(os.path.abspath(__file__)))
'''
p_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.dirname(p_dir)
sys.path.append(base_dir)

print(sys.path)

from core import main
from core.test import test
from conf import setting