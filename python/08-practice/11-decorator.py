import time
# 装饰器 <== 高阶函数 + 嵌套函数
def decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time() 
        print('*args:', *args)
        print('**kwargs:', **kwargs)
        print('run time elasped:%ds'% (end_time - start_time))
    return wrapper

@decorator
def run_func():
    a = int(input('input x:').strip(' '))
    b = int(input('input y:').strip(' '))
    print('%d**%d = %d' % (a, b, a**b))


run_func()

@decorator
def add(a,b=1):
    print('{a} + {b} = {c}'.format(a=a,b=b, c=a+b))
    print('{} + {} = {}'.format(a,b, a+b))


add(5,5)
