#!/usr/bin/python

import numpy as np


def p_a(a):
    return a[:2, -2:]


def p_b(b):
    return b[-2:]


if __name__ == '__main__':
    a = np.array([
        np.arange(1, 5),
        np.arange(11, 15),
        np.arange(21, 25)
    ])

    b = np.array([[2], [-5], [7], [10]])

    print(p_a(a))
    print(p_b(b))
