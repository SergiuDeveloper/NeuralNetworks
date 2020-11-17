#!/usr/bin/python

import numpy as np


def get_transpose(a):
	return a.T


def compute_determinant(a):
	return np.linalg.det(a)


def get_inverse(a):
	return np.linalg.inv(a)


if __name__ == '__main__':
	a = np.random.random((5, 5))

	print(get_transpose(a))

	determinant = compute_determinant(a)
	print(determinant)

	if determinant != 0:
		print(get_inverse(a))
