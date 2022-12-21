#def say_hello(e,f,p = 2, *args, **kwargs):
#    a = args 
#    b = kwargs
#    print('e=%s, f=%s, p=%s, a=%s, b=%s' %(e,f, p, a, b))
#
#say_hello(1,2,3,a=1)
#
#A = ['a','b','c']
#B = ['d','e','f']
#C = map(lambda x,y:x+y, A,B)
#print(list(C))
#
#def feibo(n):
#    a,b = 0, 1
#    c = []
#    while n > 0:
#        c.append(b)
#        a,b=b,a+b
#        n -=1
#    print(c)
#
#feibo(6)
#
#
#def outer(n):
#    def inner(n_in):
#        print('inner num is %d' % n_in)
#        return n + n_in
#    return inner
#
#a = outer(20)
#print(a(200))

def outer(func):
    def inner():
        func()
        print('come from china')
    return inner

@outer
def func1():
    print('this is mike')

func1()
