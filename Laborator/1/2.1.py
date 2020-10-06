#!/usr/bin/python

import numpy as np

a = np.array([
	np.arange(1, 5),
	np.arange(11, 15),
	np.arange(21, 25)
])

b = np.array([[2], [-5], [7], [10]])

print(a[:2, -2:])
print(b[-2:])
