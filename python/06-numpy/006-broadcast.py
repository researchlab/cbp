import numpy as np

# x = np.array([[1], [2], [3]])  # 3x1
# y = np.array([4, 5, 6])  # 1x3

# b = np.broadcast(x, y)
# print(b)  # b是一个迭代对象

# r, c = b.iters
# print(next(r), next(c))
# print(b.shape)

# print(np.broadcast_to(y, (3, 3)))
# print(y)

# c = np.arange(9).reshape(1, 3, 3)
# print(c, '\n')
# print('0 ', np.squeeze(c, axis=0))
# # # print('1 ', np.squeeze(c, axis=1))
# # print('2 ', np.squeeze(c, axis=2))
# # print('3 ', np.squeeze(c, axis=3))
# print(np.squeeze(c).shape)

# d = np.arange(6).reshape(2, 3)
# print(d)

# print(np.resize(d, (2, 4)))
# print(np.resize(d, (1, 3)))

e = np.array([5, 2, 6, 2, 7, 5, 6, 8, 2, 9])
# return_inverse 返回旧列表元素在新列表中的位置(下标)
u, indices = np.unique(e, return_inverse=True)
print('去重数组:', u, '\n')
print('去重数组下标:', indices, '\n')
print('使用下标重构原数组:', u[indices])

'''
output 
去重数组: [2 5 6 7 8 9] 

去重数组下标: [1 0 2 0 3 1 2 4 0 5] 

使用下标重构原数组: [5 2 6 2 7 5 6 8 2 9]
'''
