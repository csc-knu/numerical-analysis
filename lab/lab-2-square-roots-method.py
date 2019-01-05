#!usr/bin/env python
# -*- coding: utf-8 -*-
"""square_roots_method.py: solves the system a x = b of linear equations
with square roots method, i.e. via A = S^T D S decomposition. This file also 
contains functions to compute |A| and A^{-1} based on this decomposition."""
import numpy as np
from numpy.linalg import solve, det, inv, norm
from math import sqrt


def sign(x):
	""" :param x: real number to get the sign of """
	return (x > 0) - (x < 0)


def _norm(a, p):
	"""
	:param a: matrix to find norm of
	:param p: power of the norm, only 1 ans np.inf supported
	"""
	if p == 1:
		ax = 1
	if p == np.inf:
		ax = 0

	return np.max(np.sum(np.abs(a), axis=ax))


def s_d_decompose(a):
	""" :param a: matrix to find S^T D S decompisition of """
	n = a.shape[0]

	s, d = np.zeros((n, n)), np.zeros(n)

	for i in range(n):
		pi = float(a[i, i] - sum(s[l, i]**2 * d[l] for l in range(i)))

		d[i], s[i, i] = sign(pi), sqrt(abs(pi))

		s[i, i + 1 : n] = a[i, i + 1 : n] - \
			sum(s[l, i] * d[l] * s[l, i + 1 : n] for l in range(i))

		s[i, i + 1 : n] /= s[i, i] * d[i]

	return s, d


def square_roots_method(a, b):
	"""
	:param a: matrix from linear system to solve
	:param b: vector from linear system to solve
	"""
	n = a.shape[0]

	s, d = s_d_decompose(a)
			
	y = np.zeros(n)

	for i in range(n):
		y[i] = (b[i] - sum(s[j, i] * d[j] * y[j] for j in range(i))) / \
			(s[i, i] * d[i])

	x = np.zeros(n)

	x[-1] = y[-1] / s[-1, -1]

	for i in range(n - 1)[::-1]:
		x[i] = (y[i] - sum(s[i, j] * x[j] for j in range(i + 1, n))) / s[i, i]

	return x


def _inv(a):
	""" :param a: matrix to find the inverse of """
	n = a.shape[0]

	s, d = s_d_decompose(a)

	inverse = np.zeros((n, n))

	for k in range(n):
		b, y = np.zeros(n), np.zeros(n)
		b[k] = 1

		for i in range(n):
			y[i] = (b[i] - sum(s[j, i] * d[j] * y[j] for j in range(i))) / \
				(s[i, i] * d[i])

		inverse[-1, k] = y[-1] / s[-1, -1]

		for i in range(n - 1)[::-1]:
			inverse[i, k] = y[i] - \
				sum(s[i, j] * inverse[j, k] for j in range(i + 1, n))

			inverse[i, k] /= s[i, i]

	return inverse


def _det(a):
	""" :param a: matrix to find the determinant of """
	s, d = s_d_decompose(a)

	return np.product(np.diag(s)) ** 2 * np.product(d)


def _a(i, j):
	"""
	:param i: row of entry of a to generate
	:param j: row of entry of a to generate
	"""
	if i != j:
		return (i + j - 1) / (2 * n)
	else:
		return 10 + n + (i + j - 1) / (2 * n)


if __name__ == '__main__':
	np.set_printoptions(linewidth=90)

	n = 6

	a = np.matrix([[_a(i, j) for j in range(1, n)] for i in range(1, n)])

	a_inv, _a_inv = inv(a), _inv(a)

	b = np.arange(17, 17 + 5 * (n - 1), 5)

	x_true, x_sqrm = solve(a, b), square_roots_method(a, b)

	print(f'\nЗнайдена нами норма\n'
		f'\t||A|| = {_norm(a, 1)}\n\n')

	print(f'Знайдена бібліотечною функцією норма\n'
		f'\t||A|| = {norm(a, 1)}\n\n')

	print(f'Знайдене нами число обумовленості\n'
		f'\tcond(A) = {_norm(a, 1) * _norm(_a_inv, 1)}\n\n')

	print(f'Знайдене бібліотечною функцією число обумовленості\n'
		f'\tcond(A) = {norm(a, 1) * norm(a_inv, 1)}\n\n')

	print(f'Знайдена нами обернена матриця A^{{-1}} =\n\n'
		f'{_inv(a)}\n\n')

	print(f'Знайдена бібліотечною функцією обернена матриця A^{{-1}} =\n\n'
		f'{inv(a)}\n\n')

	print(f'Знайдена нами A^{{-1}} * A =\n\n'
		f'{a * _a_inv}\n\n')

	print(f'Знайдена бібліотечною функцією A^{{-1}} * A =\n\n'
		f'{a * a_inv}\n\n')

	print(f'Знайдений нами розв\'язок\n'
		f'\tx = {x_sqrm}\n\n')

	print(f'Знайдений бібліотечною функцією розв\'язок\n'
		f'\tx = {x_true}\n\n')

	print(f'Вектор нев\'язки \n'
		f'\tr = {x_sqrm - x_true}\n\n')

	print(f'Знайдений нами визначник\n'
		f'\t|A| = {_det(a)}\n\n')

	print(f'Знайдений бібліотечною функцією визначник\n'
		f'\t|A| = {det(a)}\n')


__author__: "Nikita Skybytskyi"
__copyright__ = "Copyright 2019, KNU"
__credits__ = ["Nikita Skybytskyi"]
__license__ = "MIT"
__version__ = "1.1"
__maintainer__ = "Nikita Skybytskyi"
__email__ = "n.skybytskyi@knu.ua"
__status__ = "Production"
