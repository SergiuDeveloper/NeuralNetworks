#!/usr/bin/python

import numpy as np

a = np.random.random(5)
b = np.matrix(np.random.random((5, 5)))

print(np.dot(a, b))
