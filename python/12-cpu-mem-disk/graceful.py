import os 
import multiprocessing


class GracefulExitEvent(object):
    def __init__(self):
        self.workers = []
        self.exit_event = multiprocessing.Event()
    def reg_worker(self, wp):
        self.workers.append(wp)
    def wait_all(self):
        while True:
            try:
                for wp in self.workers:
                    wp.join()
                print("main process(%d) exit." % os.getpid())
                break
            except Exception(ex):
                print("ex:",ex)

def worker_proc():
    print("gee:")

if __name__ == "__main__":
    print("main process(%d) start" % os.getpid())

    gee = GracefulExitEvent()

    for i in range(0, 10):
        #wp = multiprocessing.Process(target=worker_proc, args=(gee,))
        wp = multiprocessing.Process(target=worker_proc)
        wp.start()
        gee.reg_worker(wp)

    gee.wait_all()
