"""水仙花数"""

"""
【问题描述】
    如果一个d位自然数（d ≥ 3）n等于它的每个位上的数字的d次幂之和，那么该d位自然数n被称为水仙花数。
    例如：371 = 3 ^ 3 + 7 ^ 3 + 1 ^ 3
	求所有的三位水仙花数。

【设计思路】
    先分解每个位,保存到一个数组中，然后计算这个数的长度， 在套用水仙数公式求解
"""

def waterNum(n):
    t = []
    tmp = n
    while tmp > 0:
        t.append(tmp % 10) # 取余,取个位数
        tmp //=10 # 取商
    d = len(t)

    return n == sum([i ** d for i in t]) 

print('所有三位数水仙数:')
for n in range(100, 1000):
    if waterNum(n):
        print(n)
