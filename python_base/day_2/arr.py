__author__ = "JJ.sven"

import copy

names = ["0", "1", "2", "3", "4", "5", "6", "7"]

print(len(names))
# 切片操作
print(names[:3])
print(names[3:])
print(names[1::2])
print(names[1:3])
print(names[-1])
print(names[-2:])
print(names[-3:-1])

# names.append("8")
names.insert(0, "-1")
names[0] = "start"
# names.remove("start")
# del names[0]
names.pop(0)
print(names)

names.append("1")
print(names.count("1"))
print(names)
print(names.index("1"))

# names.reverse()
# names.sort(reverse=True)
# names.clear();
print(names)

names2 = ["8", "9"]
names.extend(names2)
# del names2
print(names, names2)

# 浅拷贝
names3 = names.copy()
name4 = copy.copy(names)
name5 = names[:]
name6 = list(names)  # 工厂发放
# 深拷贝
name4 = copy.deepcopy(names)
print(names3)

for n in names[::2]:
    print(n)
