from log import GetLog

logger= GetLog().get_log()

class Logic(object):
    def showlog(self):
        logger.error("showlog")

 
