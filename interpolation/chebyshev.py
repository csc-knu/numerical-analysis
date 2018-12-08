#!/usr/bin/env python
import numpy as np
import unittest
from math import sqrt, cos, pi
from typing import Callable


def interpolate_newton_equidistant(y: np.array, x_to: float, a: float or None=None, 
	b: float or None=None, n: int or None=None, h: float or None=None) -> float:
	"""
	interpolates f(x_to) given y with Newton's interpolatstion
	:param f:  
	:param a:
	:param b:
	:param n:
	:param x_to:
	:return: P_n(x_to)
	"""
	if a is None:
		a = b - h * n
	if b is None:
		b = a + h * n
	if n is None:
		n = (b - a) / h
	if h is None:
		h = (b - a) / n

	t = (x_to - a) / h

	x = np.array([((b-a)*cos((2*i+1)*pi/(2*n))+a+b)/2 for i in range(n)])

	n = x.shape[0]

	rr = np.zeros((n, n))

	rr[0] = y

	for i in range(n - 1):
		rr[i+1, :-1-i] = rr[i, 1:n-i] - rr[i, :-1-i]
	
	for _ in range(n):
		print(f'{rr[_][n-1-_]}+(x-{x[_]})*(')

	pnx, nk = 0, 1

	for k in range(n):
		pnx, nk = pnx + nk * rr[k, 0], nk * (t - k) / (k + 1)
		print(f'pnx = {pnx}, nk = {nk}')

	return pnx


class TestInterpolateNewtonEquidistant(unittest.TestCase):
	def test_0(self):
		def f(x: float) -> float:
			return 1 / 2 * (abs(x + 4) + abs(x - 4))

		a, b, n, x_to = -5, 7, 5, 0

		y = np.array([f(((b-a)*cos((2*i+1)/(2*n))*pi+a+b)/2) for i in range(n)])

		self.assertAlmostEqual(interpolate_newton_equidistant(y, x_to, a, b, n), 4, 4)

	def atest_1(self):
		def f(x: float) -> float:
			return 1 / 2 * (abs(x + 4) + abs(x - 4))

		a, b, n, x_to = -5, 7, 5, .5

		y = np.array([f(((b-a)*cos((2*i+1)/(2*n))*pi+a+b)/2) for i in range(n)])

		self.assertAlmostEqual(interpolate_newton_equidistant(y, x_to, a, b, n), 4, 4)

	def atest_2(self):
		def f(x: float) -> float:
			return 1 / 2 * (abs(x + 4) + abs(x - 4))

		a, b, n, x_to = -5, 7, 5, .25

		y = np.array([f(((b-a)*cos((2*i+1)/(2*n))*pi+a+b)/2) for i in range(n)])

		self.assertAlmostEqual(interpolate_newton_equidistant(y, x_to, a, b, n), 4, 4)

if __name__ == '__main__':
	unittest.main()
