#!/usr/bin/env python
import numpy as np
import unittest
from math import inf, sqrt


def matrix_helder_norm(a: np.matrix, p: float) -> float:
	return pow(np.sum(np.power(np.abs(a), p)), 1 / p) if p != inf else np.max(np.abs(a))


class TestMatrixHelderNorm(unittest.TestCase):
	def test_1(self):
		a = np.matrix([[1, 2, -3], [4, -5, 6], [7, 8, -9]])

		self.assertEqual(matrix_helder_norm(a, 1), 45)


	def test_2(self):
		a = np.matrix([[1, 2, -3], [4, -5, 6], [7, 8, -9]])

		self.assertAlmostEqual(matrix_helder_norm(a, 2), sqrt(285))


	def test_inf(self):
		a = np.matrix([[1, 2, -3], [4, -5, 6], [7, 8, -9]])

		self.assertEqual(matrix_helder_norm(a, inf), 9)


if __name__ == '__main__':
	unittest.main()
