#!/usr/bin/python

import numpy as np

size = 5

a = np.random.random((1, size))
b = np.random.random((1, size))

dif = np.sum(a) - np.sum(b)
if dif == 0:
	print("Vectorii au suma egala")
elif dif > 0:
	print("Primul vector are suma mai mare")
else:
	print("Al doilea vector are suma mai mare")

print(np.add(a, b))

print(np.multiply(a, b))
print(np.dot(a, np.reshape(b, (size, 1))))

print(np.sqrt(a))
print(np.sqrt(b))
