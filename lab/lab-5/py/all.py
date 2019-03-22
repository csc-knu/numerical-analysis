#!/usr/bin/env python -W ignore
import numpy as np
from scipy import integrate
import matplotlib
import matplotlib.pyplot as plt
from math import pi
from typing import Callable, List


def scalar_product_int(f1: Callable[[float], float], f2: Callable[[float], float], 
    a: float, b: float, rho: Callable[[float], float]=lambda x: 1) -> float:
    """
    :param f1: first function
    :param f2: second function
    :param a: left endpoint of the integration interval
    :param b: right endpoint of the integration interval
    :return: scalar product of f1 and f2 in L2 on [a, b]
    """
    return integrate.quad(lambda x: f1(x) * f2(x) * rho(x), a, b)[0]


def root_mean_square_approximation(n: int, a0: float, b0: float, 
    f: Callable[[float], float], phi: Callable[[int, float], float], 
    plot: bool, rho: Callable[[float], float]=lambda x: 1) -> Callable[[float], float]:
    """
    :param n: "degree" of approximation polynomial
    :param a0: left endpoint of approximation interval
    :param b0: right endpoint of approvimation interval
    :param f: function to approximate
    :param phi: system of functions which are used in approximation
    :param plot: whether to plot the true and approximation functions
    :return: approximation function
    """
    b = np.array([
        scalar_product_int(f, lambda x: phi(i, x), a0, b0, rho)
        for i in range(n)
    ])

    a = np.array([
        [
            scalar_product_int(
                lambda x: phi(i, x),
                lambda x: phi(j, x),
                a0, b0, rho
            )
            for j in range(n)
        ]
        for i in range(n)
    ])

    c = np.linalg.solve(a, b)

    def f_sol(x):
        return np.dot(c, np.array([phi(k, x) for k in range(n)]))

    if plot:
        x = np.linspace(a0, b0, 100)
        plt.figure(figsize=(20, 10))
        plt.plot(x, f_sol(x), 'r--', label='Approximation function')
        plt.plot(x, f(x), 'b.', label='True function')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.ylim((3,11))
        plt.legend()
        plt.grid(True)

    return f_sol


def root_mean_square_approximation_polinomial(n: int, a0: float, b0: float, 
    f: Callable[[float], float], plot: bool) -> Callable[[float], float]:
    """
    :param n: "degree" of approximation polynomial
    :param a0: left endpoint of approximation interval
    :param b0: right endpoint of approvimation interval
    :param f: function to approximate
    :param plot: whether to plot the true and approximation functions
    :return: approximation function
    """
    def phi(i: int, x: float) -> float:
        return x**i

    if plot:
        plt.title("Polynomial approximation")

    f_sol = root_mean_square_approximation(n + 1, a0, b0, f, phi, plot)

    if plot:
        plt.savefig('../tex/polynomial.png', bbox_inches='tight')

    print(f'Polynomial approximation error = '
        f'{integrate.quad(lambda x: (f_sol(x) - f(x))**2, a0, b0)[0]}')

    return f_sol


def rescale_function(old_a: float, old_b: float, f: Callable[[float], float], 
    new_a: float, new_b: float) -> Callable[[float], float]:
    """
    :param old_a: old leftpoint of rescaling interval
    :param old_b: right leftpoint of rescaling interval
    :param f: function to rescale
    :param new_a: old leftpoint of rescaled interval
    :param new_b: right leftpoint of rescaled interval
    :return: rescaled function
    """
    return lambda x: f((old_b - old_a) / (new_b - new_a) * (x - new_a) + old_a)


def root_mean_square_approximation_trigonometric(n: int, a0: float, b0: float, 
    f: Callable[[float], float], plot: bool) -> Callable[[float], float]:
    """
    :param n: "degree" of approximation polynomial
    :param a0: left endpoint of approximation interval
    :param b0: right endpoint of approvimation interval
    :param f: function to approximate
    :param plot: whether to plot the true and approximation functions
    :return: approximation function
    """
    a0, b0, f = -pi, pi, rescale_function(a0, b0, f, -pi, pi)

    def phi(i: int, x: float) -> float:
        return (np.sin if (i & 1) else np.cos)(((i + 1) >> 1) * x)

    if plot:
        plt.title("Trigonometric approximation")

    f_sol = root_mean_square_approximation((n << 1) + 1, a0, b0, f, phi, plot)

    if plot:
        plt.savefig('../tex/trigonometric.png', bbox_inches='tight')

    print(f'Trigonometric approximation error = '
        f'{integrate.quad(lambda x: (f_sol(x) - f(x))**2, a0, b0)[0]}')

    return f_sol


def root_mean_square_approximation_exponent(n: int, a0: float, b0: float, 
    f: Callable[[float], float], plot: bool) -> Callable[[float], float]:
    """
    :param n: "degree" of approximation polynomial
    :param a0: left endpoint of approximation interval
    :param b0: right endpoint of approvimation interval
    :param f: function to approximate
    :param plot: whether to plot the true and approximation functions
    :return: approximation function
    """
    def phi(i: int, x: float) -> float:
        return np.exp((((i if (i & 1) else -i) + 1) >> 1) * x)

    if plot:
        plt.title("Exponential approximation")

    f_sol = root_mean_square_approximation((n << 1) + 1, a0, b0, f, phi, plot)

    if plot:
        plt.savefig('../tex/exponent.png', bbox_inches='tight')

    print(f'Exponential approximation error = '
        f'{integrate.quad(lambda x: (f_sol(x) - f(x))**2, a0, b0)[0]}')

    return f_sol


def root_mean_square_approximation_chebyshev(n: int, a0: float, b0: float, 
    f: Callable[[float], float], plot: bool) -> Callable[[float], float]:
    """
    :param n: "degree" of approximation polynomial
    :param a0: left endpoint of approximation interval
    :param b0: right endpoint of approvimation interval
    :param f: function to approximate
    :param plot: whether to plot the true and approximation functions
    :return: approximation function
    """
    a0, b0, f = -1, 1, rescale_function(a0, b0, f, -1, 1)

    def phi(i: int, x: float) -> float:
        return np.cos(i * np.arccos(x))

    if plot:
        plt.title("Chebyshev approximation")

    f_sol = root_mean_square_approximation(n + 1, a0, b0, f, phi, plot,
        lambda x: 1 / np.sqrt(1 - x**2))

    if plot:
        plt.savefig('../tex/chebyshev.png', bbox_inches='tight')

    print(f'Chebyshev approximation error = '
        f'{integrate.quad(lambda x: (f_sol(x) - f(x))**2, a0, b0)[0]}')

    return f_sol


def scalar_product_discrete(f1: Callable[[float], float], f2: Callable[[float], float], 
    x: List[float]) -> float:
    """
    :param f1: first function
    :param f2: second function
    :param x: list of nodes
    :return: scalar product of f1 and f2 over x
    """
    return np.dot(list(map(f1, x)), list(map(f2, x))) / len(x)


def root_mean_square_approximation_polinomial_discrete(m: int, a0: float, 
    b0: float) -> Callable[[float], float]:
    x = np.linspace(a0, b0, m + 1)
    
    cost = [np.inf for _ in range(15)]
    for n in range(1, 15):
        b = np.array([
            scalar_product_discrete(f, lambda x: x**i, x)
        for i in range(n + 1)])

        a = np.array([[
            scalar_product_discrete( 
                lambda x: x**j, 
                lambda x: x**i,
                x) for j in range(n + 1)
        ] for i in range(n + 1)])

        c = np.linalg.solve(a, b)

        def f_sol(x):
            s = 0
            x_pow = 1
            for k in range(n + 1):
                s += c[k] * x_pow
                x_pow *= x
            return s

        def diff(x): 
            return f(x) - f_sol(x)

        cost[n] = scalar_product_discrete(diff, diff, x) / (m - n)

        print(f'n = {n}, cost = {cost[n]}')

    # true value of n
    n = 2  # cost.index(min(cost))

    b = np.array([
        scalar_product_discrete(f, lambda x: x**i, x)
    for i in range(n + 1)])

    a = np.array([[
        scalar_product_discrete(
            lambda x: x**j, 
            lambda x: x**i, 
            x) for j in range(n + 1)
    ] for i in range(n + 1)])

    c = np.linalg.solve(a, b)

    def f_sol(x):
        s = 0
        x_pow = 1
        for k in range(n + 1):
            s += c[k] * x_pow
            x_pow *= x
        return s

    def diff(x):
        return f(x) - f_sol(x)

    x = np.linspace(a0, b0, 100)
    plt.figure(figsize=(20, 10))
    plt.plot(x, f_sol(x), 'r--', label='Approximation function')
    plt.plot(x, f(x), 'b.', label='True function')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title("Polynomial discrete interpolation")
    plt.ylim((3,11))
    plt.legend()
    plt.grid(True)
    plt.savefig('../tex/discrete.png', bbox_inches='tight')

    return f_sol


def spline_interpolation(n: int, a0: float, b0: float, 
    f: Callable[[float], float]) -> None:
    x = np.linspace(a0, b0, n + 1)
    h = x[1:] - x[:-1]

    rho = 3e+2
    R = rho * np.eye(n + 1)

    H = np.zeros((n + 1, n + 1))

    for i in range(1, n):
        H[i][i - 1] = 1 / h[i - 1]
        H[i][i] = - (1 / h[i - 1] + 1 / h[i])
        H[i][i + 1] = 1 / h[i]

    a = np.zeros((n + 1, n + 1))
    b = np.zeros(n + 1)    

    for i in range(n + 1):
        if i == 0 or i == n:
            a[i, i] = 1
        else:
            a[i, i - 1] = h[i - 1] / 6
            a[i, i] = (h[i - 1] + h[i]) / 3
            a[i, i + 1] = h[i] / 6
            b[i] = (f(x[i + 1]) - f(x[i])) / h[i] - (f(x[i]) - f(x[i - 1])) / h[i - 1]

    m = np.linalg.solve(a + np.dot(H, np.dot(np.linalg.inv(R), H.T)), b)

    f_u = f(x) - np.dot(np.linalg.inv(R), np.dot(H.T, m).T)

    def f_sol(x0: float) -> float:
        for i in range(n):
            if x[i + 1] >= x0 >= x[i]:
                return m[i] * ((x[i + 1] - x0)**3) / (6 * h[i]) + \
                    m[i + 1] * ((x0 - x[i])**3) / (6 * h[i]) + \
                    (f_u[i] - m[i] * h[i]**2 / 6) * (x[i + 1] - x0) / h[i] + \
                    (f_u[i + 1] - m[i + 1] * h[i]**2 / 6) * (x0 - x[i]) / h[i]

    x1 = np.linspace(a0, b0, 100 + 1)
    y = [f_sol(xi) for xi in x1]
    plt.figure(figsize=(20, 10))
    plt.plot(x1, y, 'r--', label='Approximation function')
    plt.plot(x1, f(x1), 'b.', label='True function')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f"Spline interpolation, $\\rho_i = {rho}$")
    plt.ylim((3,11))
    plt.legend()
    plt.grid(True)
    plt.savefig(f'../tex/spline_{rho}.png', bbox_inches='tight')

    print(f'Spline approximation error = '
        f'{integrate.quad(lambda x: (f_sol(x) - f(x))**2, a0, b0)[0]}')



n, m, a0, b0 = 4, 20, -10, 10


def f(x: float) -> float:
    return (abs(x + 4) + abs(x - 4)) / 2


matplotlib.rcParams.update({'font.size': 20})

# root_mean_square_approximation_polinomial(n, a0, b0, f, True)

# root_mean_square_approximation_exponent(n, a0, b0, f, True)

# root_mean_square_approximation_trigonometric(n, a0, b0, f, True)

# root_mean_square_approximation_chebyshev(n, a0, b0, f, True)

# root_mean_square_approximation_polinomial_discrete(m, a0, b0)

spline_interpolation(m, a0, b0, f)
