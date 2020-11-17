#!/usr/bin/python

import numpy as np


def compare_vec_sum(a, b):
	dif = np.sum(a) - np.sum(b)

	if dif == 0:
		return 0
	elif dif > 0:
		return -1
	else:
		return 1


def add_vec(a, b):
	return np.add(a, b)


def multiply_scalar(a, b):
	return np.multiply(a, b)


def multiply_vectorial(a, b):
	return np.dot(a, np.reshape(b, (size, 1)))


def sqrt_vec(a):
	return np.sqrt(a)


if __name__ == '__main__':
	size = 5

	a = np.random.random((1, size))
	b = np.random.random((1, size))

	print(compare_vec_sum(a, b))

	print(add_vec(a, b))

	print(multiply_scalar(a, b))
	print(multiply_vectorial(a, b))

	print(sqrt_vec(a))
	print(sqrt_vec(b))


