"""勾股数"""

"""
【问题描述】
    满足x * x + y * y == z * z的正整数解x、y和z，被称为一组勾股数。
    求指定区间内的所有勾股数。
    	
【设计思路】
	为了去除重复的勾股数，还可以在穷举的区间中限定x < y。
	由已知条件：x、y和z是x * x + y * y = z * z的正整数解，可知：y < z，从而x < y < z。
	假设指定的区间为[a, b]，则x、y和z的下限分别为：a、x + 1和y + 1，x、y和z的上限分别为：b - 2、b - 1和b。
	因此，x的取值范围是[a, b - 2]，y的取值范围是[x + 1, b - 1]，z的取值范围是[y + 1, b]。
	通过三重循环在指定的区间内穷举x、y和z，
	在穷举的过程中，只要满足x * x + y * y == z * z，则找到一组勾股数。
"""

def gougu(a, b):
    # x范围 [a, b-2], y范围[x+1, b-1], z范围[y+1, b]
    # for range (c, d) 是左闭右开区间, 真实取值是 c 到d-1
    for x in range(a, b-1):
        for y in range(x+1, b):
            for z in range (y+1, b+1):
                if x * x + y * y == z * z:
                    # 打印勾股数
                    print(x, y ,z)

print('指定区间[{a}, {b}]内的所有勾股数是:'.format(a=1,b=20))
gougu(1, 20)

