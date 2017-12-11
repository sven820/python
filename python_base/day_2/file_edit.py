__author__ = "JJ.sven"

import os

dir_name = os.path.dirname(__file__)

ori_file = 'doc'
ori_file_p = os.path.join(dir_name, ori_file)

cache_file = '.doc.bak' #linux 名称以.开头就是隐藏文件
cache_file_p = os.path.join(dir_name, cache_file)


file = open(ori_file, 'r', encoding='utf-8')
file_bak = open(cache_file, 'w', encoding='utf-8')
for line in file:
    if 'guangzhou' in line:
        line = line.replace('guangzhou', 'jinxiaofei')
    file_bak.write(line)

file_bak.close()
file.close()

os.remove(ori_file_p)
os.rename(cache_file_p, ori_file_p)

print(os.stat(ori_file_p))


# 再删除原来的，将bak文件重命名之前的就可以了


# with open(ori_file, 'r', encoding='utf-8') as f, \
#      open(cache_file, 'r', encoding='utf-8') as f_bak:
#
#     print(f.read())
#     print(f_bak.read())
