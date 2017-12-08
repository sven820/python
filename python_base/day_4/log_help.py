__author__ = "JJ.sven"

import logging

# python 日志模块 logging


'''
format参数中可能用到的格式化串：
%(name)s Logger的名字
%(levelno)s 数字形式的日志级别
%(levelname)s 文本形式的日志级别
%(pathname)s 调用日志输出函数的模块的完整路径名，可能没有
%(filename)s 调用日志输出函数的模块的文件名
%(module)s 调用日志输出函数的模块名
%(funcName)s 调用日志输出函数的函数名
%(lineno)d 调用日志输出函数的语句所在的代码行
%(created)f 当前时间，用UNIX标准的表示时间的浮 点数表示
%(relativeCreated)d 输出日志信息时的，自Logger创建以 来的毫秒数
%(asctime)s 字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒
%(thread)d 线程ID。可能没有
%(threadName)s 线程名。可能没有
%(process)d 进程ID。可能没有
%(message)s用户输出的消息
'''
log_format = '%(asctime)s %(name)s [line:%(lineno)d] %(levelname)s %(message)s'

'''
python中时间日期格式化符号：
%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12） 
%M 分钟数（00=59）
%S 秒（00-59）

%a 本地简化星期名称
%A 本地完整星期名称
%b 本地简化的月份名称
%B 本地完整的月份名称
%c 本地相应的日期表示和时间表示
%j 年内的一天（001-366）
%p 本地A.M.或P.M.的等价符
%U 一年中的星期数（00-53）星期天为星期的开始
%w 星期（0-6），星期天为星期的开始
%W 一年中的星期数（00-53）星期一为星期的开始
%x 本地相应的日期表示
%X 本地相应的时间表示
%Z 当前时区的名称
%% %号本身

默认的时间格式为%Y-%m-%d %H:%M:%S
'''
date_fromat = '%a, %d %b %Y %H:%M:%S'
'''
filename：用指定的文件名创建FiledHandler，这样日志会被存储在指定的文件中。
filemode：文件打开方式，在指定了filename时使用这个参数，默认值为“a”还可指定为“w”。
format：  指定handler使用的日志显示格式。 
datefmt： 指定日期时间格式。 
level：   设置rootlogger（后边会讲解具体概念）的日志级别 
stream：  用指定的stream创建StreamHandler。可以指定输出到sys.stderr,sys.stdout或者文件，
          默认为sys.stderr。若同时列出了filename和stream两个参数，则stream参数会被忽略。
          
日志级别： 日志级别等级CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET
'''
logging.basicConfig(level=logging.DEBUG,
                    format=log_format,
                    datefmt=date_fromat,
                    filename='test.log',
                    filemode='w',
                    # stream=None
                    )

logging.debug('this is debug msg')
logging.warning('this is warning msg')
logging.info('this is info msg')
logging.error('this is error msg')

'''默认root log'''
root_log = logging.getLogger()
'''
log 为树形结构，子log继承父log的相关设置， handle， filter不设置话，也是继承
'''
main_log = logging.getLogger('main')
main_log.setLevel(logging.DEBUG)
sub_log = logging.getLogger('main.sub')
sub_log.setLevel(logging.WARNING)

''' handle
有多中可用的Handler：
logging.StreamHandler 可以向类似与sys.stdout或者sys.stderr的任何文件对象(file object)输出信息
logging.FileHandler 用于向一个文件输出日志信息
logging.handlers.RotatingFileHandler 类似于上面的FileHandler，但是它可以管理文件大小。当文件达到一定大小之后，它会自动将当前日志文件改名，然后创建一个新的同名日志文件继续输出
logging.handlers.TimedRotatingFileHandler 和RotatingFileHandler类似，不过，它没有通过判断文件大小来决定何时重新创建日志文件，而是间隔一定时间就自动创建新的日志文件
logging.handlers.SocketHandler 使用TCP协议，将日志信息发送到网络。
logging.handlers.DatagramHandler 使用UDP协议，将日志信息发送到网络。
logging.handlers.SysLogHandler 日志输出到syslog
logging.handlers.NTEventLogHandler 远程输出日志到Windows NT/2000/XP的事件日志 
logging.handlers.SMTPHandler 远程输出日志到邮件地址
logging.handlers.MemoryHandler 日志输出到内存中的制定buffer
logging.handlers.HTTPHandler 通过"GET"或"POST"远程输出到HTTP服务器
各个Handler的具体用法可查看参考书册：
https://docs.python.org/2/library/logging.handlers.html#module-logging.handlers
'''
fh = logging.FileHandler('main.log')
ch = logging.StreamHandler()

# 设置日志记录的级别
# fh.setLevel(logging.ERROR)
'''format'''
formatter = logging.Formatter(log_format, date_fromat)
fh.setFormatter(formatter)
ch.setFormatter(formatter)

'''filter
当然也可以直接给Logger加Filter。若为Handler加Filter则所有使用了该Handler的Logger都会受到影响。
而为Logger添加Filter只会影响到自身
'''
# filter = logging.Filter('main.sub')
# ch.addFilter(filter)
''' '''
main_log.addHandler(fh)
main_log.addHandler(ch)

'''
这里main.sub error msg 打印了两次，因为handle会把msg给父hanale再处理一次
所以sub logger可以设置自己特殊的handle 和filter等设置
'''
# sub_log.addHandler(fh)
# sub_log.addHandler(logging.StreamHandler())

main_log.debug('debug msg')
sub_log.debug('debug msg')

main_log.error('error msg')
sub_log.error('error msg')

'''
多模块使用logginglogging模块保证在同一个python解释器内，多次调用logging.getLogger('log_name')都会返回同一个logger实例，
即使是在多个模块的情况下。所以典型的多模块场景下使用logging的方式是在main模块中配置logging，
这个配置会作用于多个的子模块，然后在其他模块中直接通过getLogger获取Logger对象即可。
'''