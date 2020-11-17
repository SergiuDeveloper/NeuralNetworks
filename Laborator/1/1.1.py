#!/usr/bin/python

import math


def is_prime(x):
    if x < 2:
        return False

    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


if __name__ == '__main__':
    num = int(input())

    print(is_prime(num))
