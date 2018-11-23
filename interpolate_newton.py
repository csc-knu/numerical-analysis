#!/usr/bin/env python
import numpy as np
import unittest
from math import sqrt
from typing import Callable


def interpolate_newton(f: Callable[[float], float], x: np.array, x_to: float) -> float:
	f2 = np.vectorize(f)

	n = x.shape[0]

	rr = np.zeros((n, n))

	rr[0] = f2(x)

	for i in range(n - 1):
		rr[i+1, :-1-i] = (rr[i, 1:n-i] - rr[i, :-1-i]) / (x[1+i:] - x[:-1-i])
		
	pnx = rr[n - 1, 0]

	for i in range(n - 1)[::-1]:
		pnx = pnx * (x_to - x[i]) + rr[i, 0]
		
	return pnx


class TestInterpolateNewton(unittest.TestCase):
	def test_0(self):
		def f(x: float) -> float:
			return sqrt(sqrt(x + 2))


		x, x_to = np.array([0, 2, 4, 5, 7, 10]), 3

		self.assertAlmostEqual(interpolate_newton(f, x, x_to), 1.495, 2)


if __name__ == '__main__':
	unittest.main()
