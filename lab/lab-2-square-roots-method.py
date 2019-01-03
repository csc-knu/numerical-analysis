#!usr/bin/env python
import numpy as np
import unittest
from numpy.linalg import norm, solve, inv, det
from math import sqrt


def signum(x):
    return (x > 0) - (x < 0)


def square_roots_method(a: np.matrix, b: np.array) -> np.array:
	if a.shape[0] != a.shape[1] or a.shape[0] != b.shape[0]:
		raise ValueError('Dimensions mismatch')

	n = a.shape[0]

	for i in range(n):
		for j in range(i):
			if a[i, j] != a[j, i]:
				raise ValueError('A is not symmetric')

	s, d = np.zeros((n, n)), np.zeros((n, n))

	for i in range(n):
		pi = float(a[i, i] - sum(s[l, i]**2 * d[l, l] for l in range(i)))
		d[i, i], s[i, i] = signum(pi), sqrt(abs(pi))

		for j in range(i + 1, n):
			s[i, j] = (a[i, j] - sum(s[l, i] * d[l, l] * s[l, j] for l in range(i))) / \
				(s[i, i] * d[i, i])

	y = np.zeros(n)

	for i in range(n):
		y[i] = (b[i] - sum(s[j, i] * d[j, j] * y[j] for j in range(i))) / \
			(s[i, i] * d[i, i])

	x = np.zeros(n)

	x[-1] = y[-1] / s[-1, -1]

	print(f's = {s}\n')

	print(f'd = {d}\n')

	print(f'y = {y}\n')

	for i in range(n - 1)[::-1]:
		x[i] = (y[i] - sum(s[i, j] * x[j] for j in range(i + 1, n))) / s[i, i]

	return x


class TestSquareRootsMethod(unittest.TestCase):
	def test_0(self):
		n = 5
		a = np.matrix([[(i + j - 1) / (2 * n) if i != j else 10 + n + (i + j - 1) / (2 * n) \
			for j in range(1, 6)] for i in range(1, 6)])

		print(f'norm(a) = {norm(a, 1)}\n')

		print(f'cond(a) = {norm(a, 1) * norm(inv(a), 1)}\n')

		print(f'Знайдений бібліотечною функцією визначник det(a) = {det(a)}\n')

		print(f'a^{{-1}} = {inv(a)}\n')

		print(f'a^{{-1}} * a = {a * inv(a)}\n')

		b = np.array([17, 22, 27, 32, 37])

		x_true = solve(a, b)

		print(f'Знайдений бібліотечною функцією розв\'язок x = {x_true}\n')

		x_sqrm = square_roots_method(a, b)

		print(f'Знайдений нами розв\'язок x = {x_sqrm}\n')

		print(f'Вектор нев\'язки = {x_sqrm - x_true}\n')

		self.assertAlmostEqual(norm(x_sqrm - x_true), 0)


if __name__ == '__main__':
	print(f'\nЗнайдений нами визначник det(a) = '
		f'{(3.88587185 * 3.91118281 * 3.93494437 * 3.95622753 * 3.97439554)**2}\n')

	unittest.main()
