"""回文数"""

"""
【问题描述】
	对于某个自然数，如果从左到右读与从右到左读都是一样的，那么该自然数就被称为回文数。
    例如：12321，从左到右读与从右到左读都是12321，所以12321是回文数。
	对于任意给定的自然数，判断是否是回文数。
【设计思路】
    讲数字转换成字符串，然后通过字符串收尾比较
"""

def huiwen(n):
    tmp = str(n)
    _len = len(tmp)
    for idx in range (len(tmp)):
        if tmp[idx] != tmp[_len -idx -1]:
            print('%d 不是回文'% n)
            return 
    print('%d 是回文' % n)

huiwen(12321)
huiwen(12322)
