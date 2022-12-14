import numpy as np

# a = np.arange(8).reshape(2, 2, 2)
# print(a, '\n')
# for i in range(8):
#     print('i=', i, ' idx=', np.where(a == i))

# b = np.array([1,2])
# b.append(1)

# c = np.array([1, 2, 3])
# print(c, '\n')

# d = np.append(c, [1, 2])
# print(d, '\n')

e = np.arange(8).reshape(2, 4)

f = e.flatten(order='F')
f[1] = 3
print(e, '\n', f.flatten(order='F'))


# example 1:
# data1 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
# arr2 = np.array(data1)
# arr3 = np.asarray(data1)
# data1[1][1] = 2
# print('data1:\n', data1)
# print('arr2:\n', arr2)
# print('arr3:\n', arr3)

# example 2:
arr1 = np.ones((3, 3))
arr2 = np.array(arr1)
arr3 = np.asarray(arr1)
arr1[1] = 2
print('arr1:\n', arr1)
print('arr2:\n', arr2)
print('arr3:\n', arr3)
