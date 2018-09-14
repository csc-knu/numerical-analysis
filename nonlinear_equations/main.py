# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 10:05:30 2018

@author: Nikita Skybytskyi, OM-3

Solving Nonlinear Equations
"""

import numpy as np
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
    np.set_printoptions(precision=10)
    np.set_printoptions(suppress=True)

    if '-s' in options:
        if a >= b:
            raise BoundariesError(a, b)

    if '-m' in options:
        f = functools.lru_cache(maxsize=128)(f)

    logs = np.array([0, 0, 0])

    if f(a) * f(b) > 0:
        raise ValueError(f'f(a) * f(b) = f({a}) * f({b}) = {f(a) * f(b)} > 0')

    def step(x):
        nonlocal a, b

        if f(x) * f(a) <= 0:
            b = x
        if f(x) * f(b) <= 0:
            a = x

        return (a + b) / 2

    xi = (a + b) / 2

    if '-i' in options:
        for i in range(math.ceil(math.log2((b - a) / eps)) + 1):
            if '-l' in options:
                logs = np.vstack((logs, np.array([i, xi, f(xi)])))

            xi = step(xi)
    else:
        i = 0
        while b - a > 2 * eps:
            i += 1
            if '-l' in options:
                logs = np.vstack((logs, np.array([i, xi, f(xi)])))

            xi = step(xi)

    if '-l' in options:
        print(logs)

    return (a + b) / 2


# OK
def simple_iterate(f: types.FunctionType, x0: float, a: float, b: float, eps: float=1e-5,
                   tau: types.FunctionType=lambda x: x, options: str='-m -s -l -t -tau') -> float:
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
    np.set_printoptions(precision=10)
    np.set_printoptions(suppress=True)

    if '-1' in options and '-t' in options:
        raise ValueError('Cannot use both choices of phi simultaneously.')

    if '-1' not in options and '-t' not in options:
        raise ValueError('Choice of phi not specified in options parameter.')

    if '-s' in options:
        safety_check(a, b, x0)

    logs = np.array([0, 0, 0])

    def phi(x):
        if '-1' in options:
            return f(x) + x

        if '-tau' in options:
            return f(x) * tau(x) + x

    if '-t' in options:
        phi = threshold(phi, a, b)

    if '-m' in options:
        phi = functools.lru_cache(maxsize=128)(phi)

    xi = x0

    i = 0
    while abs(phi(xi) - xi) >= eps:
        i += 1
        if '-l' in options:
            logs = np.vstack((logs, np.array([i, xi, f(xi)])))
            print(f'{xi:10.10f}')

        xi = phi(xi)

    if '-l' in options:
        print(logs)

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
    np.set_printoptions(precision=10)
    np.set_printoptions(suppress=True)

    if '-s' in options:
        safety_check(a, b, x0)

    def phi(x):
        return tau * f(x) + x

    if '-t' in options:
        phi = threshold(phi, a, b)

    if '-m' in options:
        phi = functools.lru_cache(maxsize=128)(phi)

    logs = np.array([0, 0, 0])

    xi = x0

    i = 0
    while abs(phi(xi) - xi) >= eps:
        i += 1
        if '-l' in options:
            logs = np.vstack((logs, np.array([i, xi, f(xi)])))

        xi = phi(xi)

    if '-l' in options:
        print(logs)

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
    np.set_printoptions(precision=10)
    np.set_printoptions(suppress=True)

    if '-s' in options:
        safety_check(a, b, x0)

    def step(x):
        return x - f(x) / d(x)

    if '-t' in options:
        step = threshold(step, a, b)

    if '-m' in options:
        step = functools.lru_cache(maxsize=128)(step)

    xi = x0

    logs = np.array([0, 0, 0])

    i = 0
    while abs(step(xi) - xi) >= eps:
        i += 1
        if '-l' in options:
            logs = np.vstack((logs, np.array([i, xi, f(xi)])))

        xi = step(xi)

    if '-l' in options:
        print(logs)

    return step(xi)


# OK
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
    np.set_printoptions(precision=10)
    np.set_printoptions(suppress=True)

    if '-s' in options:
        safety_check(a, b, x0)

    def step(x):
        return x - f(x) / dx0

    if '-t' in options:
        step = threshold(step, a, b)

    if '-m' in options:
        step = functools.lru_cache(maxsize=128)(step)

    xi = x0

    logs = np.array([0, 0, 0])

    i = 0
    while abs(step(xi) - xi) >= eps:
        i += 1
        if '-l' in options:
            logs = np.vstack((logs, np.array([i, xi, f(xi)])))

        xi = step(xi)

    if '-l' in options:
        print(logs)

    return step(xi)


# OK
def secant(f: types.FunctionType, x0: float, x1: float, a: float, b: float,
           eps: float = 1e-5, options: str = '-m -l -s') -> float:
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
    :return: root of f on [a, b] if any
    """
    np.set_printoptions(precision=10)
    np.set_printoptions(suppress=True)

    if '-s' in options:
        safety_check(a, b, x0)
        safety_check(a, b, x1)

    if '-m' in options:
        f = functools.lru_cache(maxsize=128)(f)

    def step(local_now):
        nonlocal prev

        local_next = local_now - (local_now - prev) / (f(local_now) - f(prev)) * f(local_now)
        prev = local_now

        return local_next

    now, prev = x1, x0

    logs = np.array([0, 0, 0])

    i = 0
    while abs(now - prev) >= eps:
        i += 1
        if '-l' in options:
            logs = np.vstack((logs, np.array([i, now, f(now)])))

        now = step(now)

    if '-l' in options:
        print(logs)

    return now
