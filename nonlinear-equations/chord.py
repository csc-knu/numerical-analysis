#!/usr/bin/env python
""" implementation of a chord method of solving nonlinear equations with unittest """
from math import sin
from typing import Callable
import unittest


def chord(f: Callable[[float], float], a: float, b: float, m1: float, M1: float, x0: float, 
	eps: float=1e-7, kmax: int=1e3) -> float:
	"""
	solves f(x) = 0 by chord method on [a, b] with precision eps
	:param f: f
	:param a: left endpoint
	:param b: right endpoint
	:param m1: min_[a, b] |f'(x)|
	:param M1: max_[a, b] |f'(x)|
	:param x0: starting point
	:param eps: precision wanted
	:return: root of f(x) = 0
	"""
	x, x_prev, i = x0, x0 + 2 * eps, 1
	
	if f(a) < 0 and f(b) > 0:
		some_condition = True  # change
		while abs(f(x)) / m1 >= eps and abs(x - x_prev) * (M1 - m1) / m1 >= eps and i <= kmax:
			x, x_prev, i = x - f(x) / (f(b) - f(x)) * (b - x), x, i + 1

	if f(b) < 0 and f(a) > 0:
		while abs(f(x)) / m1 >= eps and abs(x - x_prev) * (M1 - m1) / m1 >= eps and i <= kmax:
			x, x_prev, i = x - f(x) / (f(x) - f(a)) * (x - a), x, i + 1

	return x


class TestChord(unittest.TestCase):
	def test_0(self):
		def f(x: float) -> float:
			return x**2 - 20 * sin(x)


		a, b, m1, M1, x0, x_star = 2, 3, 12.3229367309428, 25.7998499320089, 2, \
			2.7529466338187049383

		self.assertAlmostEqual(chord(f, a, b, m1, M1, x0), x_star)


if __name__ == '__main__':
	unittest.main()
