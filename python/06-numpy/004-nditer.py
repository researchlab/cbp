import numpy as np

a = np.arange(0, 60, 5).reshape(3, 4)
h = np.zeros(0)
for x in np.nditer(a, flags=['external_loop']):
    print(x, end=",")
    h = x
print('h', h)
# b = np.arange(6).reshape(2, 3)
# print(b, '\n')

# for x in np.nditer(b):
#     print(x, end=",")
# print('\n')
# for x in np.nditer(b.T.copy(order='C')):
#     print(x, end=',')
# print('\n')
# for x in np.nditer(b.T, order='C'):
#     print(x, end=',')
# print('\n')
# for x in np.nditer(b.T.copy(order='F')):
#     print(x, end=',')
