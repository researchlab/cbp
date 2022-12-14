import numpy as np

x = np.arange(32).reshape(8, 4)
print(x[[3, 2, 1, 7]])
print(x)
# print(x[[-4, -2, -1, -7]])
print('ix_')
print(x[np.ix_([1, 5, 7, 2], [0, 3, 1, 2])])
