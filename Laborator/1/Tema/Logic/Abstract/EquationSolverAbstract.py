#!/usr/bin/python3.8

from Models.Coefficients import Coefficients
from Models.EquationResult import EquationResult
from typing import List, Union

import abc
import re


class EquationSolverAbstract(metaclass=abc.ABCMeta):
    def __init__(self, file_name):
        self._coefficients: List[Coefficients] = EquationSolverAbstract.__retrieve_params(file_name)

    @abc.abstractmethod
    def solve_equation_system(self) -> Union[EquationResult, None]:
        pass

    @staticmethod
    def __retrieve_params(file_name):
        equations_list = EquationSolverAbstract.__get_equations_list(file_name)
        params = EquationSolverAbstract.__parse_params(equations_list)

        return params

    @staticmethod
    def __get_equations_list(file_name):
        with open(file_name, 'r') as f:
            equations = f.readlines()
            equations = map(str.strip, equations)

        return equations

    @staticmethod
    def __parse_params(equations_list):
        params = list()

        for equation in equations_list:
            match = re.search(r'(?:([^x]*)\s*x)?\s*(?:([^y]*)\s*y)?\s*(?:([^z]*)\s*z)?\s*=(.*)', equation)

            a = EquationSolverAbstract.__get_param_from_regex_match_group(match.group(1))
            b = EquationSolverAbstract.__get_param_from_regex_match_group(match.group(2))
            c = EquationSolverAbstract.__get_param_from_regex_match_group(match.group(3))
            r = eval(match.group(4))
            param = Coefficients(a, b, c, r)
            params.append(param)

        return params

    @staticmethod
    def __get_param_from_regex_match_group(regex_match_group):
        if regex_match_group is None:
            return 0

        regex_match_group = regex_match_group.strip()
        if len(regex_match_group) == 0 or regex_match_group == '+':
            return 1
        if regex_match_group == '-':
            return -1

        return eval(regex_match_group)
