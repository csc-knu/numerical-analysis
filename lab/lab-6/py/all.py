#!/usr/bin/env python
import numpy as np
from typing import Callable


def cubic_root(x: float) -> float:
	return np.array([np.power(xi, 1 / 3) if (xi >= 0) else -np.power(-xi, 1 / 3) for xi in x])


def f(x: float) -> float:
	return np.log(2 + cubic_root(x)) / cubic_root(x)


def integrate_rect(f: Callable[[float], float], a: float, b: float, h: float) -> float:
	x = np.arange(a, b + h, h)
	return h * np.sum(f((x[1:] + x[:-1]) / 2))


def apriori_error(M_2: float, a: float, b: float, h: float) -> float:
	return M_2 * h * h * (b - a) / 24


if __name__ == '__main__':
	h = 0.001

	a, b = -1, 1
	# a, b = 1, 3

	eps = 1e-5

	R_half_h = 2 * eps

	m = 2  # TODO: update to true value

	M_2 = .34

	I_h, I_half_h = integrate_rect(f, a, b, h), integrate_rect(f, a, b, h / 2)

	while abs(R_half_h) >= eps:
		h /= 2

		I_h, I_half_h = I_half_h, integrate_rect(f, a, b, h / 2)

		R_half_h = (I_half_h - I_h) / ((1 << m) - 1)

	print(
		f'apriori_error = {apriori_error(M_2, a, b, h)}\n'
		f'h             = {h}\n'
		f'I_h           = {I_h}\n'
		f'I_half_h      = {I_half_h}\n'
		f'R_half_h      = {R_half_h}'
	)
