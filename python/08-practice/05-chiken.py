"""鸡兔同笼"""

"""
【问题描述】
    在同一个笼子里有若干鸡兔，从上面数共有H个头，从下面数共有f只脚，求笼子里鸡兔的只数
【设计思路】
    设计鸡兔分别为x和y只，则可得到:
    x + y = H 
    2x + 4y = f 
    由此得知 x取值范围[1, h-1] 而 y = h -x 
"""

def chickenRabbit(h, f):
    for x in range(1,h):
        y = h -x 
        if 2 *x + 4 * y == f:
            print('鸡:%d , 兔:%d' % (x, y))
            return

chickenRabbit(35, 94)
