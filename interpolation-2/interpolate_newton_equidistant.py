#!/usr/bin/env python
import numpy as np
import unittest
from math import sqrt
from typing import Callable


def interpolate_newton_equidistant(f: Callable[[float], float], x_to: float, 
	a: float or None=None, b: float or None=None, n: int or None=None, 
	h: float or None=None) -> float:
	"""
	interpolates f(x_to) given f(x) with Newton's interpolatstion
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

	x = np.arange(a, b + h, h)

	n = x.shape[0]

	rr = np.zeros((n, n))

	rr[0] = np.vectorize(f)(x)

	for i in range(n - 1):
		rr[i+1, :-1-i] = rr[i, 1:n-i] - rr[i, :-1-i]
		
	pnx, nk = 0, 1
	
	for k in range(n):
		pnx, nk = pnx + nk * rr[k, 0], nk * (t - k) / (k + 1)

	return pnx


class TestInterpolateNewtonEquidistant(unittest.TestCase):
	def test_0(self):
		def f(x: float) -> float:
			return sqrt(sqrt(x + 2))


		a, b, n, h, x_to = 0, 10, 5, 2, 3

		self.assertAlmostEqual(interpolate_newton_equidistant(f, x_to, a, b, n, h), 1.495, 2)


if __name__ == '__main__':
	unittest.main()
