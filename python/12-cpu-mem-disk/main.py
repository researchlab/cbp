#!/usr/bin/env python 
# -*- coding: utf-8 -*-
from multiprocessing import cpu_count 
from multiprocessing import Process 
import multiprocessing
import psutil
import time 

# 让cpu满载
def loop():
    i = 0
    flag = 80
    while True:
        if psutil.cpu_percent() > flag:
            i += 1
            print('>', flag)
            if i%10 == 0:
                print('100')
                time.sleep(0.02)
                flag = 30
                i = 0
        pass 

def cpu_percent(cpu_used_percent):
    while True:
        cpu_percent = psutil.cpu_percent()
        print('cpu_percent:', cpu_percent)
        cpu_used_percent.value = cpu_percent
        print('val:', cpu_used_percent.value)
        time.sleep(1)
     
if __name__ == '__main__':
    p_lst = [] 
    core_count = cpu_count() # cpu核数
    print("core count:",core_count)
    cpu_used_percent = multiprocessing.Value("d",0.0)
    cp = Process(target=cpu_percent, args=(cpu_used_percent,))
    cp.start()
    core_count = 6 
    for i in range(core_count):
        p = Process(target=loop) #子进程调用函数
        p.start() # 启动子进程
        p_lst.append(p) # 将所有进程写入列表中
    for p in p_lst:
        p.join() #检测p是否结束，如果没有结束就阻塞到结束，否则不阻塞
    print('结束')

