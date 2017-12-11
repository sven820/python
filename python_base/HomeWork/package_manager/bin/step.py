__author__ = "JJ.sven"

import os, sys
dir_path = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.dirname(dir_path)
sys.path.append(base_dir)

# 推荐使用这种，程序开始时导入根路径，其它模块导入都用根路径+模块路径，有提示，pycharm不会报错，对应下面3
project_base_dir = os.path.dirname(os.path.dirname(base_dir))
sys.path.append(project_base_dir)


'''1'''
'''导入main 包, bao》模块》函数（要在__init__中导入相应模块）'''
# from core import main
# if __name__ == '__main__':
#     main.main.main()


'''2 导入模块 模块》函数'''
# from core.main import main
# if __name__ == '__main__':
#     main.main()

'''3 项目根路径导入，有提示, 注意要将项目根路径加入sys.path中'''
# from HomeWork.package_manager.core.main import main
# if __name__ == '__main__':
#     main.main()

'''4 动态import模块（不推荐）
    这里module是到package'''
# module = __import__('core.main')
# if __name__ == '__main__':
#     module.main.main.main()

'''5 动态import模块 (推荐)
    这里main直接到相应模块了
    '''
import importlib
main = importlib.import_module('core.main')
if __name__ == '__main__':
    main.main.main()

