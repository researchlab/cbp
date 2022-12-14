import numpy as np

import numpy as np

a = np.array([[0, 0, 0],
              [10, 10, 10],
              [20, 20, 20],
              [30, 30, 30]])
b = np.array([0, 1, 2])
# print(a + b)

# c = np.array([0, 1, 2, 3]).reshape(4, 1)
# print(c)
# print(a + c)

d = np.array([[1, 2], [3, 4]], dtype='i1')
print(d, '\n')

e = np.tile(d, (1, 2))
print(e)
