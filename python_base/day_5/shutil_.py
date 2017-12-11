__author__ = "JJ.sven"

import shutil
import os

'''http://www.cnblogs.com/wupeiqi/articles/4963027.html'''

dirp = os.path.dirname(os.path.abspath(__file__))
shutil.move(os.path.join(dirp, 'test_package/test'), dirp)