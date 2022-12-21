from multiprocessing import Process, Event, cpu_count, set_start_method
import multiprocessing
import os,signal,time,platform
import psutil

class GracefulExitException(Exception):
    @staticmethod
    def sigterm_handler(signum, frame):
        raise GracefulExitException()

class GracefulExitEvent(object):
    def __init__(self):
        self.workers = []
        self.exit_event = multiprocessing.Event()
        signal.signal(signal.SIGTERM, GracefulExitException.sigterm_handler)

    def reg_worker(self, wp):
        self.workers.append(wp)
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
                print("main process(%d) got GracefulExitException."% os.getpid())
            except Exception(ex):
                self.notify_stop()
                print("main process(%d) got unexpected Exception:%r"%(os.getpid(), ex))
                break

class CPUSimulator(object):
    def __init__(self):
        self.cpu_core_count = cpu_count() 
        self.simulated_used_percent = [0.3,0.5,0.7,0.9,0.6,0.4]
        self.cores = [ int(i * self.cpu_core_count) for i in self.simulated_used_percent ]
    def load(self, gee,i):
        print('worker', i)
        #while not gee.is_stop():
        while True:
            pass
    def cpu_used_percent(self,gee):
        while not gee.is_stop():
            print('cpu_used_percent:',psutil.cpu_percent());
            time.sleep(1)
    def simulate(self):
        while True:
            for idx, core in enumerate(self.cores):
                print('core:%d, simulated cpu used percent:%.2f'%(core, self.simulated_used_percent[idx]))
                gee = GracefulExitEvent()
                Process(target=self.cpu_used_percent, args=(gee,)).start()
                for i in range (core):
                    p = Process(target=self.load, args=(gee, i))
                    p.start()
                    gee.reg_worker(p)
                time.sleep(20)
                gee.notify_stop()
                time.sleep(5)

if __name__ == '__main__':
    if platform.system() == 'Darwin':
        set_start_method('fork')
    cpu = CPUSimulator()
    cpu.simulate()
    print('finished')
