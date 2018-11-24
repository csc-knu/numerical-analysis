#!/usr/bin/env python
import numpy as np
import unittest
from math import inf


def matrix_operator_norm(a: np.matrix, p: float) -> float:
	""" p in {1, 2, inf} """
	if p == inf:
		return np.max(sum(np.abs(a).T))
	if p == 2:
		pass
	if p == 1:
		return np.max(sum(np.abs(a))) 


class TestMatrixOperatorNorm(unittest.TestCase):
	def test_1(self):
		a = np.matrix([[1, 2, -3], [4, -5, 6], [7, 8, -9]])

		self.assertEqual(matrix_operator_norm(a, 1), 18)


	def test_2(self):
		a = np.matrix([[1, 2, -3], [4, -5, 6], [7, 8, -9]])

		self.assertAlmostEqual(matrix_operator_norm(a, 2), 0)


	def test_inf(self):
		a = np.matrix([[1, 2, -3], [4, -5, 6], [7, 8, -9]])

		self.assertEqual(matrix_operator_norm(a, inf), 24)


if __name__ == '__main__':
	unittest.main()
