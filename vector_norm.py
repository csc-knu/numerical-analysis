#!/usr/bin/env python
import numpy as np
import unittest
from math import inf, sqrt


def vector_norm(x: np.array, p: float) -> float:
	return pow(np.sum(np.power(np.abs(x), p)), 1 / p) if p != inf else np.max(np.abs(x))


class TestVectorNorm(unittest.TestCase):
	def test_1(self):
		x = np.array([1, -5, 3])

		self.assertEqual(vector_norm(x, 1), 9)


	def test_2(self):
		x = np.array([1, -5, 3])

		self.assertAlmostEqual(vector_norm(x, 2), sqrt(35))


	def test_inf(self):
		x = np.array([1, -5, 3])

		self.assertEqual(vector_norm(x, inf), 5)


if __name__ == '__main__':
	unittest.main()
