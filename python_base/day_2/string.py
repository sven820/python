__author__ = "JJ.sven"

name = 'jin xiao fei'
name1 = name[1:6]
format_name = 'i am {name}, my age is {age}'
print(name1)

print('JJJ'.capitalize())
print('xiao fei'.title())
print('jJsdfUYz'.swapcase())
print(name.lower())
print(name.upper())
print(name.count('i'))

print(name.center(50, '-'))
print(name.ljust(50, '-'))
print(name.rjust(50, '-'))

print(name.endswith('ei'))
print('xx \tss'.expandtabs(20)) # tab键空格数
print(name.find('xiao')) # 返回查找的位置
print(name[name.find('xiao'):])

print(format_name.format(name='jinxiaofei', age=18))
print(format_name.format_map({'name': 'jinxiaofei', 'age': 18}))

print('23'.isalnum())
print('asJUs'.isalpha()) # 是否是纯英文字母
print('2***fff'.isalpha())
print('12.4'.isdecimal()) # 是否是十进制的整数
print('12'.isdigit()) # 是否是整数
print('1kkL'.isidentifier()) # 是否是一个合法的标示符

print('f '.isspace())
print('24'.isnumeric())
print('My Tame'.istitle())
print('fff'.isprintable())# tty file , drive file 不能打印
print('SSS'.isupper())

print('+'.join(['1', '2', '3']))

print('\njj\njj\n'.strip()) # 去回车
print('\njj\njj\n'.lstrip()) # 去左回车
print('\njj\njj\n'.rstrip()) # 去右回车

# p = str.maketrans('abcdefg', '1234567')
# print(name.translate(p))

print(name.replace('i', 'I', -1))
print(name.rfind('i'))
print(name.find('i'))

print(name.split())
print(name.split('i'))
print(name.split('z'))
print('xxxx\nfffff'.splitlines())

print('lex li'.zfill(50))