import functools
import types
import math
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


def divide_in_two(f: types.FunctionType, a: float, b: float, eps: float=1e-5, options: str='') -> float:
    """
    :param f: function to find the root of
    :param a: (hopefully) left endpoint
    :param b: (hopefully) right endpoint
    :param eps: allowed error
    :param options: string of options, can include the following:
        -s to Swap endpoints if necessary
        -i to pre-calculate number of Iterations
        -m to Memorize already calculated values of a function
    :return: root of f on [a,b] if any
    """
    if b < a:
        if '-s' in options:
            a, b = b, a
        else:
            raise ValueError(f'b = {b} < {a} = a')

    if '-m' in options:
        f = functools.lru_cache(maxsize=3)(f)

    if f(a) * f(b) > 0:
        raise ValueError(f'f(a) * f(b) = f({a}) * f({b}) = {f(a) * f(b)} > 0')

    def step():
        nonlocal a, b
        xi = (a + b) / 2
        if f(xi) * f(a) < 0:
            b = xi
        elif f(xi) * f(b) < 0:
            a = xi
        else:
            return xi

    if '-i' in options:
        for i in range(math.ceil(math.log2((b - a) / eps)) + 1):
            s = step()
            if s is not None:
                return s
    else:
        while b - a > 2 * eps:
            s = step()
            if s is not None:
                return s

    return (a + b) / 2


def simple_iterate(f: types.FunctionType, x0: float, a: float, b:float, eps: float=1e-5,
                   tau: types.FunctionType=lambda x: x, options: str='') -> float:
    """
    :param f: function to find the root of
    :param a: (hopefully) left endpoint
    :param b: (hopefully) right endpoint
    :param x0: starting point
    :param eps: allowed error
    :param tau: function of constant sigh on [a, b]
    :param options: string of options, can include the following:
        -p1 to use 1st type of phi: phi(x) = f(x) + x
        -p2 to use second type of phi: phi(x) = x + tau(x) * f(z)
        -m to Memorize already calculated values of a function
        -s to Safety checks that xi stays in [a, b] and a < b
    :return: root of f on [a,b] if any
    """
    if '-p1' in options and '-p2' in options:
        raise ValueError('Cannot use both choices of phi simultaneously.')

    if '-p1' not in options and '-p2' not in options:
        raise ValueError('Choice of phi not specified in options parameter.')

    if '-s' in options:
        if a >= b:
            raise ValueError('Invalid boundaries, a > b.')

        if  x0 < a or x0 > b:
            raise ValueError('Starting point not in [a, b].')

    phi = None

    if '-p1' in options:
        phi = lambda x: f(x) + x

    if '-p2' in options:
        phi = lambda x: f(x) * tau(x) + x

    if '-s' in options:
        phi = lambda x: phi(x) < a if x < a else (phi(x) > b if x > b else phi(x))

    if '-m' in options:
        phi = functools.lru_cache(maxsize=128)(phi)

    xi = x0
    while abs(phi(xi) - xi) >= eps:
        xi = phi(xi)

    return phi(xi)
