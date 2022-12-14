import numpy as np

# print(bin(13), '\n')
# print(np.bitwise_and([1, 2, 3], [1, 2, 0]))  # output [1 2 0]
# print(np.bitwise_and(1, 2))  # output 0

# print(np.bitwise_or(13, 17)) # ouput 29

# print('13 的位反转，其中 ndarray 的 dtype 是 uint8：')
# print(np.invert(np.array([13], dtype=np.uint8))) # ouput [242]

# print('将 10 左移两位：')
# print(np.left_shift(10, 2))  # output 40

# print('将 40 右移两位：')
# print(np.right_shift(40, 2)) # output 10


# a = np.array([[3, 7, 5], [8, 4, 3], [2, 4, 9]])
# print(np.amin(a))
# print('\n', np.amax(a))

# print('\n', np.amax(a, axis=1))

b = np.array([20, 65, 70, 80])
print(np.median(b))
