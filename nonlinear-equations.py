import os

version = os.environ['version']
develop, production = version == 'dev', version == 'prod'


class Function:
    def __init__(self, local_function):  # local_ not to shadow built-in name function
        if production:
            raise NotImplementedError('Function.__init__ not implemented')
        if develop:
            self._function = local_function

    @property
    def function(self):
        return self._function


class NonlinearFunction(Function):
    def __init__(self, nonlinear_function):
        if production:
            raise NotImplementedError('NonlinearFunction.__init__ not implemented')
        if develop:
            Function.__init__(self, nonlinear_function)
            self._nonlinear_function = nonlinear_function

    @property
    def nonlinear_function(self):
        return self._nonlinear_function


class Equation:
    def __init__(self, local_function):  # local_ not to shadow built-in name function
        if production:
            raise NotImplementedError('Equation.__init__ not implemented')
        if develop:
            self._function = local_function

    @property
    def function(self) -> Function:
        return self._function

    def solve(self) -> float:
        if production:
            raise NotImplementedError('Equation.solve not implemented')
        if develop:
            equation_solver = EquationSolver(self)
            return equation_solver.solution


class NonlinearEquation(Equation):
    def __init__(self, nonlinear_function):
        if production:
            raise NotImplementedError('NonlinearEquation.__init__ not implemented')
        if develop:
            Equation.__init__(self, nonlinear_function)
            self._nonlinear_function = nonlinear_function

    @property
    def nonlinear_function(self) -> NonlinearFunction:
        return self._nonlinear_function

    def solve(self) -> float:
        if production:
            raise NotImplementedError('NonlinearEquation.solve not implemented')
        if develop:
            nonlinear_equation_solver = NonlinearEquationSolver(self)
            return nonlinear_equation_solver.solution


class Solver:
    def __init__(self):
        raise NotImplementedError('Solver.__init__ not implemented')


class EquationSolver(Solver):
    def __init__(self, equation):
        if production:
            raise NotImplementedError('EquationSolver.__init__ not implemented')
        if develop:
            Solver.__init__(self)
            self._equation = equation

    @property
    def equation(self) -> Equation:
        return self._equation

    @property
    def solution(self) -> float:
        raise NotImplementedError('EquationSolver.solution not implemented')


class NonlinearEquationSolver(EquationSolver):
    def __init__(self, nonlinear_equation):
        if production:
            raise NotImplementedError('NonlinearEquationSolver.__init__ not implemented')
        if develop:
            EquationSolver.__init__(self, nonlinear_equation)
            self._nonlinear_equation = nonlinear_equation

    @property
    def nonlinear_equation(self) -> NonlinearEquation:
        return self._nonlinear_equation

    @property
    def solution(self) -> float:
        raise NotImplementedError('NonlinearEquationSolver.solution not implemented')
