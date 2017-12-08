__author__ = "JJ.sven"

dic = {'key': 'value'}

info = {'001': 20, '002': 30, '003': 50, '004': 100}
# info.pop('001')
# print(info)
# info.popitem()  # 随机删除一个
# print(info)
del info['004']
print('004' in info) # 判断某个键值在不，python2用法，info.has_key('004)

value2 = info.get('002')
print(type(value2))

info.setdefault('005', 200) # 没有取到，重新创建，并设定默认值
print(info)
info.setdefault('003', 99)


print(info.values())
print(info.items())

info2 = {'001': 19, '009': 999}
info.update(info2)
print(info)

c = dict.fromkeys([1, 2, 3], {'key': 'value'})
c[1]['key'] = 'default'
print(c) # 初始化字典，注意内部是浅拷贝

for k in info:
        print(k, info[k])
for k, v in info.items():
        print(k, v)

