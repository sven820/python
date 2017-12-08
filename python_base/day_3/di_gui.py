__author__ = "JJ.sven"

# 递归一定要有退出条件

def fact(n):
    if n == 1:
        return n
    return n * fact(n-1)

print(fact(10))

