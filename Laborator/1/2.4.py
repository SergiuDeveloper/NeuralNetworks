#!/usr/bin/python

import numpy as np


def scalar_product(a, b):
    return np.dot(a, b)


if __name__ == '__main__':
    a = np.random.random(5)
    b = np.random.random((5, 5))

    print(scalar_product(a, b))
