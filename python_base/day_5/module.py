__author__ = "JJ.sven"

import sys, os
'''执行本模块，系统会将本模块目录自动加入sys.path中去'''
print(sys.path)

'''这样写本模块—__init__会被调用, 有提示'''
from day_5 import test_package
from day_5.test_package import module
module.fun1()
'''这样写本模块—__init__不会被调用, 但没提示'''
# import test_package
# test_package.module.fun1()
# test_package.module.fun1()

