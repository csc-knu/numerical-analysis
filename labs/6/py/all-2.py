#!/usr/bin/env python

import numpy as np
from scipy import integrate
from typing import Callable

m = 2
eps = 1e-6


def f(x: float) -> float:
    return np.log(2 + np.cbrt(x)) / np.cbrt(x)


def g(x: float) -> float:
    pass


def  psi(x: float) -> float:
    pass


def integrate_rect(h: float, a: float, b: float, fun: Callable[[float], float]) -> float:
    x = np.arange(a, b, h)
    return np.sum(h * fun((x[1:] + x[:-1]) / 2))


def apriori_error(h: float, M_2: float) -> float:
    return M_2 * h * h * (b - a) / 24


if __name__ == "__main__":
    print()
    
    a, b = -1, 1
    h = 0.2
    delta = eps

    g_value = integrate.quad(f, -delta, delta)[0]
    print(f'g(x) = {g_value}')

    I_h = integrate_rect(h, a, b, f)
    I_h_half = integrate_rect(h / 2, a, b, f)
    I_h_half = ((1 << m) * I_h_half - I_h) / ((1 << m) - 1)
    R_h_half = (I_h_half - I_h) / ((1 << m) - 1)

    while abs(R_h_half) >= eps:
        h = h / 2
        I_h = I_h_half
        I_h_half = integrate_rect(h / 2, a, b, f)
        I_h_half = ((1 << m) * I_h_half - I_h) / ((1 << m) - 1)
        R_h_half = (I_h_half - I_h) / ((1 << m) - 1)

    print(
        f'\tIntegral value: {I_h}\n'
        # f'\tI + g: {I_h + g_value}\n'
        f'\tAposteriori error R(h): {eps / 2 + R_h_half}\n'
        f'\th: {h}\n'
    )

    M_2 = 2e9
    h = 0.2
    
    while apriori_error(h, M_2) >= eps:
        h /= 2
    
    print(
        f'\tIntegral value f: {integrate_rect(h, a, b, f)}\n'
        # f'\tIntegral value: {g_value + integrate_rect(h, a, b, f)}\n'
        f'\tApriori error: {apriori_error(h, M_2)}\n'
        f'\th: {h}\n'
    )
