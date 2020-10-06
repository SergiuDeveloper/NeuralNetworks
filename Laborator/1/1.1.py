#!/usr/bin/python

import math

def isPrime(x):
	if x < 2:
		return False

	for i in range(2, (int)(math.sqrt(x)) + 1):
		if x % i == 0:
			return False
	return True

num = int(input())

print(isPrime(num))
