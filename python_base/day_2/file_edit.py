__author__ = "JJ.sven"

file = open('doc', 'r', encoding='utf-8')
file_bak = open('doc.bak', 'w', encoding='utf-8')
for line in file:
    if 'guangzhou' in line:
        line = line.replace('guangzhou', 'jinxiaofei')
    file_bak.write(line)

file_bak.close()
file.close()

# 再删除原来的，将bak文件重命名之前的就可以了

with open('doc', 'r', encoding='utf-8') as f, \
     open('doc.bak', 'r', encoding='utf-8') as f_bak:

    print(f.read())
    print(f_bak.read())
