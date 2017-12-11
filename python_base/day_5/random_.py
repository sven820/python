__author__ = "JJ.sven"

import random

print(random.random())
print(random.uniform(1, 3))

# 含首尾
print(random.randint(1, 3))
# 不含尾
print(random.randrange(1, 3))

# 随机一个
print(random.choice(['li', 'jj', 2]))

# 取2个
print(random.sample(['li', 'jj', 2], 2))

# 洗牌
l = [1, 2, 3, 4, 5]
random.shuffle(l)
print(l)

def randCode():
    checkCode = ''

    for i in range(5):
        if i == random.randrange(0, 5):
            if i % 2 == 0:
                checkCode += chr(random.randint(65, 90))
            else:
                checkCode += chr(random.randint(99, 122))
        else:
            checkCode += str(random.randint(0, 9))
    print(checkCode)

randCode()


