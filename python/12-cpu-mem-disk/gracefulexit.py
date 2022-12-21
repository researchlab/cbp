#-*- coding: UTF-8 -*-

import os 
import signal 
import multiprocessing

# Python 允许程序自行引发异常，使用 raise 语句即可
# raise 语句有如下三种常用的用法：
# raise：单独一个 raise。该语句引发当前上下文中捕获的异常(比如在 except 块中)，或默认引发 RuntimeError 异常。
# raise 异常类名称：raise 后带一个异常类名称。该语句引发指定异常类的默认实例。
# raise 异常类名称(描述信息)：在引发指定异常的同时，附带异常的描述信息。
# 上面三种用法最终都是要引发一个异常实例(即使指定的是异常类，实际上也是引发该类的默认实例)，raise 语句每次只能引发一个异常实例。
class GracefulExitException(Exception):
    @staticmethod
    def sigterm_handler(signum, frame):
        raise GracefulExitException()
    pass

class GracefulExitEvent(object):
    def __init__(self):
        self.workers = []
        self.exit_event = multiprocessing.Event()
        # Use signal handler to throw exception which can be caught 
        # by worker process to allow graceful exit.
        signal.signal(signal.SIGTERM, GracefulExitException.sigterm_handler)
        pass
    def reg_worker(self, wp):
        self.workers.append(wp)
        pass

    def is_stop(self):
        return self.exit_event.is_set()

    def notify_stop(self):
        self.exit_event.set()

    def wait_all(self):
        while True:
            try:
                for wp in self.workers:
                    wp.join()

                print("main process(%d) exit." % os.getpid())
                break
            except GracefulExitException:
                self.notify_stop()
                print("main process(%d) got GracefulExitException." %
                        os.getpid())
            except Exception(ex):
                self.notify_stop()
                print("main process(%d) got unexpected Exception: %r"
                        %(os.getpid(), ex))
                break 
        pass

def worker_proc(gee):
    print("worker")
    #import sys, time 
    #print("worker(%d) start..." % os.getpid())
    #try:
    #    while not gee.is_stop():
    #        print (".")
    #        time.sleep(1)
    #    else:
    #        print ("")
    #        print ("worker process(%d) got exit event." % os.getpid())
    #        print ("worker process(%d) do cleanup..." % os.getpid())
    #        time.sleep(1)
    #        print("[%d] 3" % os.getpid())
    #        time.sleep(1)
    #        print("[%d] 2" % os.getpid())
    #        time.sleep(1)
    #        print("[%d] 1" % os.getpoid())
    #except GracefulExitException:
    #    print ("worker(%d) got GracefulExitException" % os.getpid())
    #except Exception(ex):
    #    print ("Exception:",ex)
    #finally:
    #    print ("worker(%d) exit." % os.getpid())
    #    sys.exit(0)

if __name__ == "__main__":
    import sys 
    print ("main process(%d) start" % os.getpid())

    gee = GracefulExitEvent()

    # Start some workers process and run forever 
    for i in range(0, 10):
        wp = multiprocessing.Process(target=worker_proc, args=(gee,))
        wp.start()
        gee.reg_worker(wp)

    gee.wait_all()
    sys.exit(0)

