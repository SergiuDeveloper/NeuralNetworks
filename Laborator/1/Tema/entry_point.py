#!/usr/bin/python3.8

from Logic.EquationSolverNumpy import EquationSolverNumpy
from Logic.EquationSolverNoNumpy import EquationSolverNoNumpy

import math


if __name__ == '__main__':
    equation_solver_numpy = EquationSolverNumpy('input.txt')
    equation_result_numpy = equation_solver_numpy.solve_equation_system().get_result()

    print(equation_result_numpy)

    equation_solver_no_numpy = EquationSolverNoNumpy('input.txt')
    equation_result_no_numpy = equation_solver_no_numpy.solve_equation_system().get_result()

    print(equation_result_no_numpy)

    for i in range(len(equation_result_numpy)):
        for j in range(len(equation_result_numpy[i])):
            assert(math.isclose(equation_result_numpy[i][j], equation_result_no_numpy[i][j]))
