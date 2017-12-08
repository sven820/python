__author__ = "JJ.sven"


'''这里加入core_path, 是为了，core下其它模块相互间导入能直接import， 不用导入根路径方式, 
   参见main内my的导入方式，但这种没提示'''
import os, sys
core_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(core_path)

# 注意package 每次被from 或者 improt 都会被执行一次，某些情况下需要注意
print('core __init__')