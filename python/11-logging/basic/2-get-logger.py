import logging 

#1.创建日志收集器

#my_log = logging.getLogger('py')
my_log = logging.getLogger(__name__)
my_log.setLevel('DEBUG') #设置采集等级
#2.设置输出渠道
#2-1 可以同时设置两个输出渠道
sh = logging.StreamHandler() # 2-1-1 控制台输出并设置等级
sh.setLevel('DEBUG')
fh = logging.FileHandler('logout.txt') # 2-1-2 文件输入
fh.setLevel('DEBUG')
#2-2 设置日志字符串格式
format = logging.Formatter("%(levelname)s-%(name)s-%(asctime)s:%(message)s")
#2-2-1 两种输出渠道都设置format格式
sh.setFormatter(format)
fh.setFormatter(format)
#2-3 给日志收集器设置输出渠道
my_log.addHandler(sh)
my_log.addHandler(fh)

# 使用日志收集器采集日志
my_log.debug('debug')
my_log.info('info')
my_log.warning('warning')
my_log.error('error')

'''
2.2 创建日志收集器和设置输出渠道
（一）创建日志收集器
logging.getLogger('py')   py即收集器的名称，会在文件/控制台输出；如果不传名称，则默认使用RootLogger；
（二）设置输出渠道
FileHandler：文件输出；
需要指定filename；模式默认是a(追加)，模式同open函数；
setLevel指定输出的等级；
StreamHandler：控制台输出；
setLevel指定输出的等级；
'''
