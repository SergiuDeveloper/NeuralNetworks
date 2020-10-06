#!/usr/bin/python3.8

from typing import List, Tuple


class EquationResult(object):
    def __init__(self, equation_result):
        self.__result = equation_result

    def get_result(self) -> List[Tuple[float, float, float]]:
        return self.__result
