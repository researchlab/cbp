from multiprocessing import Process, cpu_count, Pool, Manager,Value
#from multiprocessing import set_start_method
import os,sys,gc,time,platform,psutil,logging

log = logging.getLogger(__name__) 
######### CPU simulator 
class CPUSimulator(object):
    def __init__(self,
            simulated_used_percent=[35,50,75,90,95,63,40,25],
            opt_delay=1, opt_interval=3600):
        self.cpu_core_count = cpu_count() 
        self.simulated_used_percent = simulated_used_percent 
        self.cores = [ int(i * self.cpu_core_count/100) for i in self.simulated_used_percent ]
        self.opt_interval = opt_interval
        self.opt_delay = opt_delay
        self.show()
    def show(self):
        log.info('############ CPU Simulator')
        log.info('# simulated_used_percent=%s'%(self.simulated_used_percent,))
        log.info('# simulated_used_cores=%s'%(self.cores,))
        log.info('# opt_interval=%d, opt_delay=%d'%(self.opt_interval,self.opt_delay))
        log.info('##########################')
    def cpu_used_percent(self, target_percent):
        while True:
            log.info('current, cpu used percent:%.1f, target:%.1f'
                    %(psutil.cpu_percent(interval=5), target_percent.value));
    def load(self, i):
        #print('worker start:',i)
        while True:
            pass
    def simulate(self):
        target_percent = Value('d', self.simulated_used_percent[0])
        Process(target=self.cpu_used_percent, args=(target_percent,)).start()
        while True:
            for idx, core in enumerate(self.cores):
                log.info('while, core:%d, simulated cpu used percent:%.1f'%(core, self.simulated_used_percent[idx]))
                target_percent.value = self.simulated_used_percent[idx]
                pool =Pool(processes=core)
                for i in range(core):
                    pool.apply_async(self.load,(i,))
                time.sleep(self.opt_interval)
                pool.terminate()
                time.sleep(self.opt_delay)

######### Memory simulator
class MemSimulator(object):
    def __init__(self,simulated_used_percent = [65,70,85,92,80,55,32,45],
            opt_interval=3600, opt_delay=5):
        self.memory = []
        self.simulated_used_percent = simulated_used_percent
        self.opt_interval = opt_interval 
        self.opt_delay = opt_delay
        self.show()
    def show(self):
        log.info('############ Mem Simulator')
        log.info('# simulated_used_percent=%s'%(self.simulated_used_percent))
        log.info('# opt_interval=%d, opt_delay=%d'%(self.opt_interval,self.opt_delay))
        log.info('##########################')
    def mem_used_percent(self, target_percent):
        while True:
            log.info('current, mem used percent:%.1f, target:%.1f' %(psutil.virtual_memory()[2],target_percent.value))
            time.sleep(self.opt_delay)
    def load(self, percent):
        while True:
            if psutil.virtual_memory()[2] <= percent:
                 self.memory.append(' '*1024*1024*100) # 100MB
                 #print('memory append 100MB')
                 time.sleep(1)
                 continue
            time.sleep(self.opt_delay)
    def unload(self):
        #print('len(mem)01:',len(self.memory))
        #del self.memory[:]
        #print('len(mem)02:',len(self.memory))
        gc.collect()

    def simulate(self):
        target_percent = Value('d', self.simulated_used_percent[0])
        Process(target=self.mem_used_percent, args=(target_percent,)).start()
        while True:
            for idx, percent in enumerate(self.simulated_used_percent):
                target_percent.value = percent
                pool = Pool(processes=1)
                pool.apply_async(func=self.load,args=(percent,))
                time.sleep(self.opt_interval)
                pool.terminate()
                self.unload()
                time.sleep(self.opt_delay)

############ disk simulator
class DiskSimulator(object):
    def __init__(self, size=5,simulated_used_percent =
            [50,75,80,92,88,65,55,32,20,45],opt_interval=3600, opt_delay=5):
        self.dir = '/tmp/simulator' + time.strftime("%Y-%m-%d-%H", time.localtime())
        self.file_prefix='eat-disk-'
        self.size = size
        if self.size <= 1:
            self.size = 1
        self.write_str='*'*1024*1024*self.size #5MB
        self.simulated_used_percent = simulated_used_percent 
        self.file_nums = sys.maxsize
        self.opt_interval = opt_interval # 1 hours 
        self.opt_delay = opt_delay # s
        self.show()
        pass
    def show(self):
        log.info('############ Disk Simulator')
        log.info('# simulated_used_percent=%s'%(self.simulated_used_percent,))
        log.info('# opt_interval=%d, opt_delay=%d'%(self.opt_interval,self.opt_delay))
        log.info('# simulator file write dir=%s'%(self.dir,))
        log.info('# file prefix=%s'%(self.file_prefix,))
        log.info('# single file size=%dMB'%self.size)
        log.info('###########################')
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
                    log.error('error:%s'%(ex))
            else:
                log.info('finished,%s, percent:%d'%(psutil.disk_usage('/'), percent))
                break
    def unload(self):
        if not os.path.isdir(self.dir):
            log.error('path doesnt exist:%s'%(self.dir))
            return
        try:
            file_list = os.listdir(self.dir)
        except PermissionError as e:
            log.error('permission denied with{}'.format(e))
            return
        log.info('file_list:%d'%(len(file_list)))
        for filename in file_list:
            path = os.path.join(self.dir, filename)
            log.info('delete:%s'%(path))
            os.remove(path)
            time.sleep(self.opt_delay)

    def disk_used_percent(self, target_percent):
        while True:
            log.info('current, disk usage:%s, target:%.1f' %(psutil.disk_usage('/'), target_percent.value))
            time.sleep(self.opt_delay)
    def simulate(self):
        target_percent = Value('d', self.simulated_used_percent[0])
        Process(target=self.disk_used_percent, args=(target_percent,)).start()
        while True:
            for idx, percent in enumerate(self.simulated_used_percent):
                target_percent.value = percent
                pool = Pool(processes=1)
                pool.apply_async(self.load,(percent,))
                time.sleep(self.opt_interval)
                pool.terminate()
                time.sleep(self.opt_delay)
                self.unload()
                time.sleep(self.opt_delay)

class Log(object):
    def __init__(self, debug=False):
        self.logger = logging.getLogger(__name__)
        self.FMT = '%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s: %(message)s'
        self.DATEFMT = '%Y-%m-%d %H:%M:%S'
        self.formatter = logging.Formatter(fmt=self.FMT, datefmt=self.DATEFMT)
        self.log_filename='{0}{1}.log'.format('/tmp/','simulator')
        self.logger.addHandler(self.get_file_handler(self.log_filename))
        if debug:
            self.logger.addHandler(self.get_console_handler())
        self.logger.setLevel(logging.DEBUG)
    def get_file_handler(self,filename):
        file_handler = logging.FileHandler(filename, encoding='utf-8')
        file_handler.setFormatter(self.formatter)
        return file_handler
    def get_console_handler(self):
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(self.formatter)
        return console_handler

if __name__ == '__main__':
    DEBUG = False
    if len(sys.argv) >=2:
        if "debug" in sys.argv[1]:
            DEBUG = True
            print('mode:DEBUG')
    log = Log(debug=DEBUG).logger
    log.info('simulator start working')
    if platform.system() == 'Darwin':
        #set_start_method('fork')
        pass

    simulators = [CPUSimulator(), MemSimulator(), DiskSimulator()]
    process = []
    for simulator in simulators:
        p = Process(target=simulator.simulate)
        p.start() 
        process.append(p)
    for p in process:
        p.join()
    log.info('simulator finished')
