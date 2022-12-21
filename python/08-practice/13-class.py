class Cat:
    age = 20 # 这个值会被下面的值覆盖
    def __init__(self, name,age):
        self.name = name 
        self.age = age 
    def eat(self):
        print('eat fish')
    def print_info(self):
        print('%s 的年龄是%s'%(self.name, self.age))


tom = Cat('tom',18) # 这个参数必须传递, 否则报缺少参数错误
tom.print_info()
