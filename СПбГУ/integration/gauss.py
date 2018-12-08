#!/usr/bin/env python
import numpy as np
import unittest
from typing import Callable
from math import sqrt, cos, pi


def integration_gauss(f: Callable[[float], float], n: int) -> float:
	""" n in {} 1, 2, 3 """
	if n == 1:
		return 2 * f(0)
	if n == 2:
		f(-1 / sqrt(3)) + f(1 / sqrt(3))
	if n == 3:
		return 5 / 9 * f(-sqrt(3 / 5)) + 8 / 9 * f(0) + 5 / 9 * f(sqrt(3 / 5))


def integration_gauss_like(f: Callable[[float], float], n: int, mu: np.array) -> float:
	""" n = 2 """
	a1, a2 = (mu[0] * mu[3] - mu[1] * mu[2]) / (mu[1]**2 - mu[0] * mu[2]), \
		(mu[2]**2 - mu[1] * mu[3]) / (mu[1]**2 - mu[0] * mu[2])

	x1, x2 = (-a1 - sqrt(a1**2 - 4 * a2)) / 2, (-a1 + sqrt(a1**2 - 4 * a2)) / 2

	A1, A2 = (mu[1] - x2 * mu[0]) / (x1 - x2), (mu[1] - x1 * mu[0]) / (x1 - x2)

	return A1 * f(x1) + A2 * f(x2)


def integration_meler(f: Callable[[float], float], n: int) -> float:
	return pi / n * sum(f(cos((2 * k + 1) / (2 * n) * pi)) for k in range(n))


if __name__ == '__main__':
    unittest.main()
