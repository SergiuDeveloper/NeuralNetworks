#!/usr/bin/python

import numpy as np

a = np.matrix(np.random.random((5, 5)))
print(a.T)

a_det = np.linalg.det(a)
print(a_det)
if a_det != 0:
	a_adjoint = a.H
	a_inverse = 1 / a_det * a_adjoint
	print(a_inverse)
