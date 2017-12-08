__author__ = "JJ.sven"


'''这里导入本模块下的做法 是针对于，外部只导入本包的话，外部通过packgename.main.func()调用时候
    
   如果是做开源模块，这里可以import包内的接口模块，表示这些都是暴露的接口
   
   参见step中1 main包的导入方式
'''
from . import main