import numpy as np

a = np.zeros((3,3))
b = np.zeros((3,3))
c = np.zeros((3,3))
d = np.zeros((3,3))
e = np.zeros((3,3))
print(a)
print()
a[1:, :2] = 1
print(a)
print()

b[:, 2:] = 1
print(b)
print()
c[:2, :] = 1
print(c)

d[:2, [0, 2]] = 1
print(d)
