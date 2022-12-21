import logging 

logging.basicConfig(filename='logout.txt',
        filemode='a',
        format='%(levelname)s-%(name)s-%(asctime)s:%(message)s',
        level='INFO',
        datefmt='%Y-%m-%d')


logging.info('info')
logging.warning('warning')
logging.error('error')

'''
2、改变输出的级别
2.1 使用basicConfig()方法
如果logger没有指定处理器，则会默认使用basicConfig，在里面可以对日志进行一些设置。该方法传关键字参数，看下常用的参数：

filename：文件名;新建一个文件处理器FileHandler。并且把日志输出到该文件，此时日志不再在控制台输出;
filemode：打开文件的方式;如果指定了filename，则可以指定该参数;默认a，表示追加;w，表示覆盖;
format：指定日志输出的字符串格式;例如：format='%(levelname)s-%(name)s-%(asctime)s: %(message)s'
datefmt：指定输出的时间格式;例如：datefmt='%Y-%m-%d'
level：指定最低输出日志的等级；例如：level='INFO' 则INFO及以上级别的日志均能被输出
stream：用例初始化一个StreamHandler；如果filename存在，则程序忽略stream;
encoding：指定filname时，可以通过该参数设置编码;
'''
