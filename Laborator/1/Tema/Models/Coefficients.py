#!/usr/bin/python3.8

class Coefficients(object):
    def __init__(self, a, b, c, r):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__r = r

    def get_a(self):
        return self.__a

    def get_b(self):
        return self.__b

    def get_c(self):
        return self.__c

    def get_r(self):
        return self.__r
