__author__ = "JJ.sven"

import sys
import os
import day_2.mod2
# from day_1 import var


print(sys.path)  # 环境变量
#
print(sys.argv)  # 参数
print(sys.argv[0])


cmd_res = os.system("ls")  # 执行shell命令
print(cmd_res)
# cmd_res 返回码


cmd_res = os.popen("ls").read()
print(cmd_res)


