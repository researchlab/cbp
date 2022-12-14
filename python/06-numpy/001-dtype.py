import numpy as np

# dt = np.dtype('a3')
# print(dt)

# dt = "1234"
# print(dt)

a = np.arange(5)
print(a)

rows = np.array([[0, 0], [3, 3]])
print(rows)

x = np.array([[0,  1,  2], [3,  4,  5], [6,  7,  8], [9,  10,  11]])
print(x)
print(x[[0, 0, 3, 3], [0, 2, 0, 2]])
print(x[np.array([[0, 0], [3, 3]]), np.array([[0, 2], [0, 2]])])
