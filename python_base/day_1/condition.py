# Author:JJ.sven

a = 1
if a == 1:
    print("true")
else:
    print("false")


while a > 1:
    print("true")
else:
    print("while end ---------- \n")

for i in range(2):
    print("loop", i)
else:
    print("for end ---------- \n")

for i in range(0, 10, 2):
    if i == 4:
        continue;
    if i == 8:
        break;
    print("loop", i)
else:
    print("for end ---------- \n")

# 三元运算符
b = 1 if a > 1 else 2
print(b)