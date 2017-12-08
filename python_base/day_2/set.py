__author__ = "JJ.sven"

# 集合 {} ,集合是无序的
list_1 = [1, 3, 2, 4, 3, 2, 1, 9, 10]
list_2 = [1, 11, 3, 3]
list_3 = [1, 3]

set_1 = set(list_1)
set_2 = set(list_2)
set_3 = set(list_3)

# 交集
print('交集')
print(set_1.intersection(set_2))
print(set_1 & set_2)
print(set_1.isdisjoint(set_2))

# 并集
print('并集')
print(set_1.union(set_2))
print(set_1 | set_2)
# 差集
print('差集')
print(set_1.difference(set_2))
print(set_1 - set_2)
print(set_2.difference(set_1))
print(set_2 - set_1)
# 对称差集
print('对称差集')
print(set_1.symmetric_difference(set_2))
print(set_1 ^ set_2)
# 子集
print('子集')
print(set_2.issubset(set_1))
print(set_3.issubset(set_1))
print(set_1.issuperset(set_2))

# 基本操作
print('基本操作')

set_3.add(100)
print(set_3)

set_3.update([100, 101, 102])
print(set_3)

set_3.remove(102)
print(set_3)

set_3.discard(109)  # 安全删除元素
if 109 in set_3:
    set_3.remove(109)
if 109 not in set_3:
    set_3.add(109)
    print(set_3)

print(set_3.pop())
print(set_3)
