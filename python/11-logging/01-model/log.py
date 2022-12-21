import logging 
import os 


class GetLog(object):
    logger = None

    @classmethod
    def get_log(cls):
        if cls.logger is None:
            print('init log')
            logpath="./logs"
            cls.logger = logging.getLogger(__name__)
            cls.logger.setLevel(logging.INFO)
            if not os.path.isdir(logpath):
                os.makedirs(logpath)

            fd =logging.FileHandler(filename='/'.join([logpath,"test.log"]),encoding='utf-8',mode='a')
            fd.setFormatter(logging.Formatter(fmt='%(asctime)s %(levelname)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S'))
            cls.logger.addHandler(fd)
            
        return cls.logger
 

