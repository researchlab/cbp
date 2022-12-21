
#!/usr/bin/env python
# coding=utf-8
# logging模块打印log日志到文件和屏幕
# Log级别：CRITICAL(50)、ERROR(40)、WARNING(30)、INFO(20)、DEBUG(10)、NOTSET(0)

import logging,os,time

class GetLog(object):
    logger=None
    path='/tmp/log'
    filename='app'

    @classmethod
    def set(cls, 
            path='/tmp/log',
            filename='app',
            time_suffix=False):
        print('self.path:',cls.path)
        cls.path=path
        print('0self.path:',cls.path)
        cls.filename=filename
        if time_suffix:
            cls.time_suffix = time.strftime("%Y-%m-%d", time.localtime())

    @classmethod
    def get_log(cls,record=__name__):
        if cls.logger is None:
            print('path:',cls.path)
            print('filename:',cls.filename)
