from multiprocessing import Process, cpu_count, set_start_method, Pool
import os,sys,gc,time,platform
import psutil

######### CPU simulator 
class CPUSimulator(object):
    def __init__(self, simulated_used_percent=[0.3,0.5,0.75,0.9,0.95,0.63,0.4,0.25]):
        self.cpu_core_count = cpu_count() 
        self.simulated_used_percent = simulated_used_percent 
        self.cores = [ int(i * self.cpu_core_count) for i in self.simulated_used_percent ]
    def cpu_used_percent(self):
        while True:
            print('cpu used percent:',psutil.cpu_percent(interval=5));

    def load(self, i):
        print('worker start:',i)
        while True:
            pass

    def simulate(self):
        Process(target=self.cpu_used_percent).start()
        while True:
            for idx, core in enumerate(self.cores):
                print('core:%d, simulated cpu used percent:%.2f'%(core, self.simulated_used_percent[idx]))
                pool =Pool(processes=core)
                for i in range(core):
                    pool.apply_async(self.load,(i,))
                time.sleep(3600)
                pool.terminate()
                time.sleep(1)

######### Memory simulator
class MemSimulator(object):
    def __init__(self):
        self.memory = []
        self.simulated_used_percent = [65,70,85,92,80,55,32,45]
    def mem_used_percent(self):
        while True:
            print('mem used percent:', psutil.virtual_memory()[2])
            time.sleep(5)
    def load(self, percent):
        while True:
            if psutil.virtual_memory()[2] <= percent:
                 self.memory.append(' '*1024*1024*100) # 一次吃100MB
                 time.sleep(1)
                 continue
            time.sleep(2)

    def unload(self):
        print('len(mem)01:',len(self.memory))
        self.memory.clear()
        print('len(mem)02:',len(self.memory))
        gc.collect()

    def simulate(self):
        Process(target=self.mem_used_percent).start()
        while True:
            for idx, percent in enumerate(self.simulated_used_percent):
                pool = Pool(processes=1)
                pool.apply_async(self.load,(percent,))
                time.sleep(10)
                pool.terminate()
                self.unload()
                time.sleep(5)

############ disk simulator
class DiskSimulator(object):
    def __init__(self):
        self.dir = '/tmp/simulator' + time.strftime("%Y-%m-%d-%H", time.localtime())
        self.file_prefix='eat-disk-'
        self.write_str='*'*1024*1024*5 #5MB
        self.simulated_used_percent = [50,75,80,92,88, 65,55,32,20,45]
        self.file_nums = sys.maxsize
        self.opt_interval = 1 # 1 hours 
        self.opt_delay = 1 # s
        pass
    def path_exists_make(self):
        if os.path.exists(self.dir):
            pass 
        else:
            os.makedirs(self.dir)
    def load(self, percent):
        self.path_exists_make()
        for i in range(1, self.file_nums):
            if psutil.disk_usage('/')[3] < percent:
                try:
                    file =os.path.join(self.dir,self.file_prefix+time.strftime("%Y%m%d%H%M%S",time.localtime()))
                    f = open(file, 'w+')
                    f.write(self.write_str)
                    f.flush()
                    f.close()
                    time.sleep(1)
                except Exception(ex):
                    print('error:',ex)
            else:
                print('finished,', psutil.disk_usage('/'), ' percent:', percent)
                break
    def unload(self):
        if not os.path.isdir(self.dir):
            print('path doesnt exist', self.dir)
            return
        try:
            file_list = os.listdir(self.dir)
        except PermissionError as e:
            print('您没有打开{}的权限'.format(e))
            return
        print('file_list:', len(file_list))
        for filename in file_list:
            path = os.path.join(self.dir, filename)
            print('delete:',path)
            os.remove(path)
            time.sleep(self.opt_delay)

    def disk_used_percent(self):
        while True:
            print('disk usage:', psutil.disk_usage('/'))
            time.sleep(5)
    def simulate(self):
        Process(target=self.disk_used_percent).start()
        while True:
            for idx, percent in enumerate(self.simulated_used_percent):
                pool = Pool(processes=1)
                pool.apply_async(self.load,(percent,))
                time.sleep(20)
                pool.terminate()
                time.sleep(self.opt_delay)
                self.unload()
                time.sleep(5)

if __name__ == '__main__':
    if platform.system() == 'Darwin':
        set_start_method('fork')
    #cpu = CPUSimulator()
    mem = MemSimulator()
    #mem.simulate()
    #cpu.simulate()
    disk = DiskSimulator()
    disk.simulate()
    print('finished')
