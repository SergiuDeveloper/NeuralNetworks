#!/usr/bin/python3.8

from Logic.Abstract.EquationSolverAbstract import EquationSolverAbstract
from Models.EquationResult import EquationResult
from typing import Union

import numpy as np


class EquationSolverNumpy(EquationSolverAbstract):
    def __init__(self, file_name):
        super().__init__(file_name)

    def solve_equation_system(self) -> Union[EquationResult, None]:
        coefficients_matrix = np.array([
            [self._coefficients[0].get_a(), self._coefficients[0].get_b(), self._coefficients[0].get_c()],
            [self._coefficients[1].get_a(), self._coefficients[1].get_b(), self._coefficients[1].get_c()],
            [self._coefficients[2].get_a(), self._coefficients[2].get_b(), self._coefficients[2].get_c()]
        ])

        results_matrix = np.array([
            [self._coefficients[0].get_r()],
            [self._coefficients[1].get_r()],
            [self._coefficients[2].get_r()]
        ])

        inverse_coefficients_matrix = np.linalg.inv(coefficients_matrix)

        equation_result_nested_list = np.matmul(inverse_coefficients_matrix, results_matrix).tolist()

        equation_result = EquationResult(equation_result_nested_list)

        return equation_result
