from multiprocessing import Process, Event 
import time,random

def worker(name, event):
    while not event.is_set():
        print('Process_%s is ready' % name)
        event.wait() # 阻塞
    print('Process_%s is running' % name)

if __name__ == '__main__':
    event = Event()
    for i in range(0, 2):
        Process(target=worker, args=(i, event)).start()
    time.sleep(random.randint(1,3))
    event.set()
