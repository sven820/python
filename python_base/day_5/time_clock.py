__author__ = "JJ.sven"

import time, datetime

'''time'''
# 实践戳，s
print(time.time())

# 时区 东八区，为-，比世界标准时间早
print(time.timezone)

# 返回与utc时间的时间差,以秒计算\
print(time.altzone)
# 是否使用了夏令时
print(time.daylight)

#
# time.sleep(.1)

'''
tm_isdst 夏令时
(tm_year=2017, tm_mon=12, tm_mday=8, tm_hour=11, tm_min=23, tm_sec=4, tm_wday=4, tm_yday=342, tm_isdst=0)
'''
# localtime 转为本地
t = time.localtime()
print(t, '\n', type(t))
print(t.tm_year)
# gmtime 时间戳转time_struct, 转为utc
print(time.gmtime(time.time()))
# time_struct转时间戳
print(time.mktime(t))

# strftime 格式化时间字符串
print(time.strftime('%Y-%m-%d %H:%M:%S', t))

# strptime 格式化字符串转时间time_struct
print(time.strptime('2017-12-08 11:51:40', '%Y-%m-%d %H:%M:%S'))


print(time.asctime(t))
print(time.ctime())

'''datetime'''

print(datetime.datetime.now())
print(datetime.datetime.now() + datetime.timedelta(3)) #当前时间+3天
# print(datetime.datetime.now() + datetime.timedelta(-3)) #当前时间-3天
# print(datetime.datetime.now() + datetime.timedelta(hours=3)) #当前时间+3小时
# print(datetime.datetime.now() + datetime.timedelta(minutes=30)) #当前时间+30分
print(datetime.datetime.now().timestamp())