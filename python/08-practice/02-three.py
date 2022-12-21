"""不重复的三位数"""

"""
【问题描述】
    统计0-9这10个数字可以组成多少个不重复的三位数

【设计思路】
    根据排列组合的数学知识可知: 0-9这10个数字可以组成不重复的三位数个数为: 9* 9
    * 8 = 648, 这三个数的取值范围分别是[1,9], [0, 9] 和[0,9]

"""

def three():
    counter = 0
    for a in range (1, 10):
        for b in range(10):
            for c in range(10):
                if a !=b and b != c and c !=a:
                    counter += 1
    print(counter)

three()
