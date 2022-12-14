import numpy
# # 01 一维数组
# a = numpy.array([1, 2, 3])
# print(a)
# print(type(a))

# # 02 多维数组
# b = numpy.array([[1, 2, 3], [4, 5, 6]])
# print(b)

# # 指定数据类型
# c = numpy.array([2, 4, 6, 8], dtype='complex')
# print(c)

# 03 ndim 查看数组纬度, ndmin 指定维度
# arr = numpy.array([[1, 2, 3, 4], [4, 5, 6, 7], [9, 10, 11, 23]])
# print(arr.ndim)

# d = numpy.array([1, 2, 3, 4, 5], ndmin=2)
# print(d)
# print(d.ndim)

# 04 reshape 数组变纬
# e = numpy.array([[1, 2], [3, 4], [5, 6]])
# print('原数组', e)
# e = e.reshape(2, 3)
# print('新数组', e)

array1 = numpy.array([1, 2, 3, 4, 5])
array2 = array1
array3 = array1[1:3]
array4 = array1[:]
array5 = array1.copy()
array6 = array1[1:4].copy()

array1[1] = 88
array5[0] = 55
array6[2] = 66

print('array1', array1)
print('array2', array2)
print('array3', array3)
print('array4', array4)
print('array5', array5)
print('array6', array6)
print('id(array1)', id(array1))
print('id(array2)', id(array2))
print('id(array3)', id(array3))
print('id(array4)', id(array4))
print('id(array5)', id(array5))
print('id(array6)', id(array6))
