#!/usr/bin/python3.8

from Logic.Abstract.EquationSolverAbstract import EquationSolverAbstract
from Models.EquationResult import EquationResult
from typing import Union


class EquationSolverNoNumpy(EquationSolverAbstract):
    def __init__(self, file_name):
        super().__init__(file_name)

    def solve_equation_system(self) -> Union[EquationResult, None]:
        coefficients_matrix = [
            [self._coefficients[0].get_a(), self._coefficients[0].get_b(), self._coefficients[0].get_c()],
            [self._coefficients[1].get_a(), self._coefficients[1].get_b(), self._coefficients[1].get_c()],
            [self._coefficients[2].get_a(), self._coefficients[2].get_b(), self._coefficients[2].get_c()]
        ]

        determinant = EquationSolverNoNumpy.__compute_determinant(coefficients_matrix)
        if determinant == 0:
            return None

        results_matrix = [
            [self._coefficients[0].get_r()],
            [self._coefficients[1].get_r()],
            [self._coefficients[2].get_r()]
        ]

        matrix_of_minors = EquationSolverNoNumpy.__compute_matrix_of_minors(coefficients_matrix)
        matrix_of_cofactors = EquationSolverNoNumpy.__compute_matrix_of_cofactors(matrix_of_minors)
        adjoint_matrix = EquationSolverNoNumpy.__compute_adjoint_matrix(matrix_of_cofactors)
        inverse_matrix = EquationSolverNoNumpy.__compute_inverse_matrix(adjoint_matrix, determinant)

        equation_result_nested_list = EquationSolverNoNumpy.__scalar_product(inverse_matrix, results_matrix)

        equation_result = EquationResult(equation_result_nested_list)

        return equation_result

    @staticmethod
    def __compute_determinant(coefficients_matrix):
        determinant = \
            coefficients_matrix[0][0] * coefficients_matrix[1][1] * coefficients_matrix[2][2] + \
            coefficients_matrix[1][0] * coefficients_matrix[2][1] * coefficients_matrix[0][2] + \
            coefficients_matrix[2][0] * coefficients_matrix[0][1] * coefficients_matrix[1][2] - \
            coefficients_matrix[0][2] * coefficients_matrix[1][1] * coefficients_matrix[2][0] - \
            coefficients_matrix[0][1] * coefficients_matrix[1][0] * coefficients_matrix[2][2] - \
            coefficients_matrix[0][0] * coefficients_matrix[2][1] * coefficients_matrix[1][2]

        return determinant

    @staticmethod
    def __compute_minor_determinant(coefficients_matrix):
        determinant = \
            coefficients_matrix[0][0] * coefficients_matrix[1][1] - \
            coefficients_matrix[0][1] * coefficients_matrix[1][0]

        return determinant

    @staticmethod
    def __compute_matrix_of_minors(coefficients_matrix):
        matrix_of_minors = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]

        for i in range(3):
            for j in range(3):
                minor_matrix = [
                    [coefficients_matrix[i2][j2] for j2 in range(3) if j2 != j]
                    for i2 in range(3) if i2 != i
                ]

                matrix_of_minors[i][j] = EquationSolverNoNumpy.__compute_minor_determinant(minor_matrix)

        return matrix_of_minors

    @staticmethod
    def __compute_matrix_of_cofactors(matrix_of_minors):
        matrix_of_cofactors = matrix_of_minors

        for i in range(3):
            for j in range(3):
                if (i + j) % 2 == 1:
                    matrix_of_cofactors[i][j] = matrix_of_cofactors[i][j] * -1

        return matrix_of_cofactors

    @staticmethod
    def __compute_adjoint_matrix(matrix_of_cofactors):
        adjoint_matrix = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]

        for i in range(3):
            for j in range(3):
                adjoint_matrix[i][j] = matrix_of_cofactors[j][i]

        return adjoint_matrix

    @staticmethod
    def __compute_inverse_matrix(adjoint_matrix, determinant):
        inverse_matrix = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]

        for i in range(3):
            for j in range(3):
                inverse_matrix[i][j] = adjoint_matrix[i][j] / determinant

        return inverse_matrix

    @staticmethod
    def __scalar_product(a, b):
        prod = list()

        for line_iter in range(len(a)):
            prod_line = list()

            for column_iter in range(len(b[0])):
                value = 0
                for el_iter in range(len(b)):
                    value += a[line_iter][el_iter] * b[el_iter][column_iter]

                prod_line.append(value)
            prod.append(prod_line)

        return prod
