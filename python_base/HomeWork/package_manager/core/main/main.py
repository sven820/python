__author__ = "JJ.sven"


'''注意要将根路径加入sys.path'''
from HomeWork.package_manager.core.home import home

'''这里已经在core的__init__导入了路径'''
from core.my import my

print('main')

def main():
    print('main func')
    home.home()
    my.my()