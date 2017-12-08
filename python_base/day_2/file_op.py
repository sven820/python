__author__ = "JJ.sven"


'''
w 以写方式打开，
a 以追加模式打开 (从 EOF 开始, 必要时创建新文件)
r+ 以读写模式打开
w+ 以读写模式打开 (参见 w )
a+ 以读写模式打开 (参见 a )
rb 以二进制读模式打开
wb 以二进制写模式打开 (参见 w )
ab 以二进制追加模式打开 (参见 a )
rb+ 以二进制读写模式打开 (参见 r+ )
wb+ 以二进制读写模式打开 (参见 w+ )
ab+ 以二进制读写模式打开 (参见 a+ )
'''

'''
# 文件句柄
file = open('doc', 'r', encoding='utf-8')
# 全读
doc = file.read()
lines = file.readlines()
print(type(file), type(doc), type(lines))
print(doc)

file.seek(0) # 游标回到起始位置
# 读行
# line = file.readline()
# str = file.read(5)
print(file.tell()) # 当前游标位置
for line in file:
    print(line.strip())
print(file.tell())

print(file.encoding)

file.close()

# mode 'w'写模式, 覆盖原文件，/ 'a'追加，默认tell（）在末尾
file2 = open('doc2', 'w', encoding='utf-8')
file2.write("\nself write self write self write \n")
file2.write("self write self write self write ")

file2.flush() # 强制刷新，更新写文件

print(file2.truncate(20)) # 截断
file2.close()

# 读写模式， 文件必须存在， 写为追加模式
file3 = open('doc3', 'r+', encoding='utf-8')
print(file3.read())

# file3.write('hello'.center(50, '-') + '\n')
# print(file3.read())

file3.seek(5)
file3.write('ttttt') # seek后指定位置写，会覆盖原文件内容
file3.read()
file3.close()

# 写读模式, 覆盖原文件
file4 = open('doc4', 'w+', encoding='utf-8')
file4.write('doc4'.center(50, '-') + '\n')
file4.write('doc4'.center(50, '-') + '\n')

file4.seek(10)
print(file4.tell()) # seek后指定位置写，会覆盖原文件内容
file4.write('test')

file4.close()

# 追加读模式, 默认tell（）在末尾
file5 = open('doc5', 'a+', encoding='utf-8')
file5.write('doc5'.center(50, '-') + '\n')
file5.write('doc5'.center(50, '-') + '\n')
file5.seek(0)
# file5.readline()
print(file5.tell())
file5.write('test')

file5.close()

# 二进制读， 'rb'
file6 = open('doc', 'rb')
print(file6.readline())
print(file6.readline())
'''

# 二进制写， 'wb'
file7 = open('doc', 'wb')
file7.write('hello world ---!!!'.encode())
file7.close()