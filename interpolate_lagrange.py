#!/usr/bin/env python
import numpy as np
import unittest
from math import sqrt
from typing import Callable


def interpolate_lagrange(f: Callable[[float], float], x: np.array, x_to: float) -> float:
	"""
	interpolates f(x_to) given f(x) with Lagrange's interpolatstion
	:param f:  
	:param x:
	:param x_to:
	:return: P_n(x_to)
	"""
	fx = np.vectorize(f)(x)

	d, x_to_d = np.matrix(x).T - x, x_to - x

	pnx = sum(fx[k] * np.product(np.hstack((x_to_d[:k], x_to_d[k+1:]))) / 
		np.product(np.hstack((d[k,:k], d[k,k+1:]))) for k in range(x.shape[0]))

	return float(pnx)

class TestInterpolateLagrange(unittest.TestCase):
	def test_0(self):
		def f(x: float) -> float:
			return sqrt(sqrt(x + 2))


		x, x_to = np.array([0, 2, 4, 5, 7, 10]), 3

		self.assertAlmostEqual(interpolate_lagrange(f, x, x_to), 1.495, 2)


if __name__ == '__main__':
	unittest.main()
