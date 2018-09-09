import functools
import types
import math


class BoundariesError(ValueError):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'Invalid boundaries, a = {self.a} >= {self.b} = b.'


class StartingPointError(ValueError):
    def __init__(self, a, b, x0):
        self.a = a
        self.b = b
        self.x0 = x0

    def __str__(self):
        return f'Starting point x0 = {self.x0} not in [a, b] = [{self.a}, {self.b}].'


def safety_check(a: float, b: float, x0: float):
    if a >= b:
        raise BoundariesError(a, b)

    if x0 < a or x0 > b:
        raise StartingPointError(a, b, x0)


def threshold(func, low, high):

    @functools.wraps(func)
    def thr(*args, **kwargs):
        if func(*args, **kwargs) < low:
            return low

        if func(*args, **kwargs) > high:
            return high

        return func(*args, **kwargs)

    return thr


def divide_in_two(f: types.FunctionType, a: float, b: float, eps: float=1e-5, options: str='-s -m -i -l') -> float:
    """
    :param f: function to find the root of
    :param a: (hopefully) left endpoint
    :param b: (hopefully) right endpoint
    :param eps: allowed error
    :param options: string of options, can include the following:
        -i to pre-calculate number of Iterations
        -m to Memorize functions
        -l to Log the execution
        -s to Safety check
    :return: root of f on [a,b] if any
    """
    if '-s' in options:
        if a >= b:
            raise BoundariesError(a, b)

    if '-m' in options:
        f = functools.lru_cache(maxsize=3)(f)

    if f(a) * f(b) > 0:
        raise ValueError(f'f(a) * f(b) = f({a}) * f({b}) = {f(a) * f(b)} > 0')

    def step(x):
        nonlocal a, b
        if '-l':
            print(f'{x:10.10f}')
        if f(x) * f(a) < 0:
            b = x
        elif f(x) * f(b) < 0:
            a = x
        else:
            return x

    xi = (a + b) / 2
    if '-i' in options:
        for i in range(math.ceil(math.log2((b - a) / eps)) + 1):
            if step(xi) is not None:
                return xi
    else:
        while b - a > 2 * eps:
            if step(xi) is not None:
                return xi

    return (a + b) / 2


def simple_iterate(f: types.FunctionType, x0: float, a: float, b: float, eps: float=1e-5,
                   tau: types.FunctionType=lambda x: x, options: str='-1 -m -s -l -t -tau') -> float:
    """
    :param f: function to find the root of
    :param a: (hopefully) left endpoint
    :param b: (hopefully) right endpoint
    :param x0: starting point
    :param eps: allowed error
    :param tau: function of constant sigh on [a, b]
    :param options: string of options, can include the following:
        -1 to use 1st type of phi: phi(x) = f(x) + x
        -tau to use tau in construction of phi: phi(x) = x + tau(x) * f(z)
        -m to Memorize functions
        -l to Log the execution
        -s to Safety check
        -t to Threshold functions
    :return: root of f on [a,b] if any
    """
    if '-1' in options and '-t' in options:
        raise ValueError('Cannot use both choices of phi simultaneously.')

    if '-1' not in options and '-t' not in options:
        raise ValueError('Choice of phi not specified in options parameter.')

    if '-s' in options:
        safety_check(a, b, x0)

    phi = None

    if '-1' in options:
        phi = lambda x: f(x) * tau(x) + x

    if '-tau' in options:
        phi = lambda x: f(x) * tau(x) + x

    if '-t' in options:
        phi = threshold(phi, a, b)

    if '-m' in options:
        phi = functools.lru_cache(maxsize=128)(phi)

    xi = x0
    while abs(phi(xi) - xi) >= eps:
        if '-l' in options:
            print(f'{xi:10.10f}')
        xi = phi(xi)

    return phi(xi)


def relaxate(f: types.FunctionType, x0: float, a: float, b: float,
             eps: float = 1e-5, tau: float = 1, options: str = '-m -s -l -t') -> float:
    """
    :param f: function to find the root of
    :param a: (hopefully) left endpoint
    :param b: (hopefully) right endpoint
    :param x0: starting point
    :param eps: allowed error
    :param tau: constant
    :param options: string of options, can include the following:
        -m to Memorize functions
        -l to Log the execution
        -s to Safety check
        -t to Threshold functions
    :return: root of f on [a, b] if any
    """
    if '-s' in options:
        safety_check(a, b, x0)

    def phi(x):
        return tau * f(x) + x

    if '-t' in options:
        phi = threshold(phi, a, b)

    if '-m' in options:
        phi = functools.lru_cache(maxsize=128)(phi)

    xi = x0
    while abs(phi(xi) - xi) >= eps:
        if '-l' in options:
            print(f'{xi:10.10f}')
        xi = phi(xi)

    return phi(xi)


def newton(f: types.FunctionType, d: types.FunctionType, x0: float, a: float, b: float,
           eps: float = 1e-5, options: str = '-m -s -l -t') -> float:
    """
    :param f: Function to find the root of
    :param d: Derivative of f
    :param a: (hopefully) left endpoint
    :param b: (hopefully) right endpoint
    :param x0: starting point
    :param eps: allowed error
    :param options: string of options, can include the following:
        -m to Memorize functions
        -l to Log the execution
        -s to Safety check
        -t to Threshold functions
    :return: root of f on [a, b] if any
    """
    if '-s' in options:
        safety_check(a, b, x0)

    def step(x):
        return x - f(x) / d(x)

    if '-t' in options:
        step = threshold(step, a, b)

    if '-m' in options:
        step = functools.lru_cache(maxsize=128)(step)

    xi = x0
    while abs(step(xi) - xi) >= eps:
        if '-l' in options:
            print(f'{xi:10.10f}')
        xi = step(xi)

    return step(xi)


def modified_newton(f: types.FunctionType, dx0: float, x0: float, a: float, b: float,
                    eps: float = 1e-5, options: str = '-m -l -s') -> float:
    """
    :param f: Function to find the root of
    :param dx0: Derivative of f at x0
    :param a: (hopefully) left endpoint
    :param b: (hopefully) right endpoint
    :param x0: starting point
    :param eps: allowed error
    :param options: string of options, can include the following:
        -m to Memorize functions
        -l to Log the execution
        -s to Safety check
        -t to Threshold functions
    :return: root of f on [a, b] if any
    """
    if '-s' in options:
        safety_check(a, b, x0)

    def step(x):
        return x - f(x) / dx0

    if '-t' in options:
        step = threshold(step, a, b)

    if '-m' in options:
        step = functools.lru_cache(maxsize=128)(step)

    xi = x0
    while abs(step(xi) - xi) >= eps:
        if '-l' in options:
            print(f'{xi:10.10f}')
        xi = step(xi)

    return step(xi)


def secant(f: types.FunctionType, x0: float, x1: float, a: float, b: float,
           eps: float = 1e-5, options: str = '-m -l -s -t') -> float:
    """
    :param f: Function to find the root of
    :param a: (hopefully) left endpoint
    :param b: (hopefully) right endpoint
    :param x0: starting point
    :param x1: second point
    :param eps: allowed error
    :param options: string of options, can include the following:
        -m to Memorize functions
        -l to Log the execution
        -s to Safety check
        -t to Threshold functions
    :return: root of f on [a, b] if any
    """
    if '-s' in options:
        safety_check(a, b, x0)
        safety_check(a, b, x1)

    if '-m' in options:
        f = functools.lru_cache(maxsize=128)(f)

    def step(now):
        nonlocal prev
        next = now - (now - prev) / (f(now) - f(prev)) * f(now)
        prev = now
        return next

    if '-t' in options:
        step = threshold(step, a, b)

    now, prev = x1, x0
    while abs(now - prev) >= eps:
        if '-l' in options:
            print(f'{now:10.10f}')
        step(now)

    return now
