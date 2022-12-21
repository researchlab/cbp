import logging 

logging.info("info")
logging.warning("warning")
logging.error("error")

'''
上述代码仅会在控制台输出：

WARNING:root:warning
ERROR:root:error

因为默认仅输出WARNING及以上级别的日志。常用的级别由高到低有：CRITICAL、ERROR、WARNING、INFO、DEBUG；

输出的格式默认为：

%(levelname)s:%(name)s:%(message)s
-levelname：级别名称；
-name：日志收集器的名称，默认为root；
-message：日志内容；
'''
