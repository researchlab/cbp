
import logic
from log import GetLog

logger= GetLog().get_log()
def call():
    l = logic.Logic()
    l.showlog()

if __name__ == '__main__':
    logger.info("test001")
    call()
