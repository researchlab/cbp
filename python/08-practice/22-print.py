# print('Hi % s, your score is %d' % ('Bart', 90))
# name = 'customized'
# print(name[2:5]) # sto
# print(name[3:0:-1]) # tsu

# 字符串查找
# tmp = "hello world"
# print(tmp.count("l"))  # 计算字符的个数,  output: 3
# print(tmp.find('l'))  # 从左边开始找字符的第一个索引, output: 2
# print(tmp.rfind('l'))  # 右边找第一个索引, output: 9
# print(tmp.index('l'))  # 同上 output: 2,  不建议使用;
# print(tmp.rindex('l'))  # 同上 9

# 字符串分割
# tmp001 = "hello\nworld\npython\n"
# print(tmp001)
'''
output:
hello
world
python
'''
# print(tmp001.partition('0'))
# partition 分割成前中后三块，如果不存在，则后两块为空
# output: ('hello\nworld\npython\n', '', '')

# print(tmp001.partition('o'))
# output: ('hell', 'o', '\nworld\npython\n')

# print(tmp001.rpartition('l'))
# output: ('hello\nwor', 'l', 'd\npython\n')

# print('h e l l \nworld'.split())
# 如果没有添加分割字符，则以制表符(空格，\n 作为分割对象)
# output: ['h', 'e', 'l', 'l', 'world']

# print(tmp001.split('0'))
# 如果分割字符不存在， 则不会分割
# output: ['hello\nworld\npython\n']

# split 要点
# 1.如果没有指定分割字符，则以制表符分割;
# 2.分割字符不会包含在分割列表中; 如果需要包含在分割列表中 用partition
# 3.如果分割字符不存在，则返回只包含一个没有分割的字符的数组;

# 字符串的替换
# print('hello'.replace('l', 'w'))
# output: hewwo
# print('hello'.replace('w', 'w'))
# output: hello , 如果不存在则不替换
# print('hello'.replace('l', 'w', 1))
# 指定替换次数
# output: hewlo

# 字符串变形
# print('hellO'.upper())  # HELLO
# print('HELLo'.lower())  # hello
# print('hEllO'.swapcase())  # HeLLo
# print('hello,world'.title())  # Hello,World  每个单词首字母都大写
# print('hello world'.capitalize())  # Hello world 只有首个单词首字母大写
# print('for\tis\tcool'.expandtabs(10))  # 将制表符转换成指定个数的空格

# 字符串判断
print('123'.isalnum())  # True
print('aaa'.isalnum())  # True
print('1l2l'.isalnum())  # True
print(''.isalnum())  # False
print('abdcd'.isalpha())
print(''.isalpha())  # False
print('111'.isdigit())
print('0'.isnumeric())  # True
print('Hello, World'.istitle())  # True
print('s  '.isspace())  # False
print('with'.startswith('wi'))  # True
print('ends'.endswith('ds'))  # True
