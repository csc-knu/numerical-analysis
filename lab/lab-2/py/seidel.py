#!usr/bin/env python
# -*- coding: utf-8 -*-
"""seidel.py: solves the system a x = b of linear equations with seidel 
algortihm."""
import numpy as np
from numpy.linalg import inv, norm, solve


def seidel(a, b, eps, max_iterations=1e3):
	"""
	:param a: matrix from linear system to solve
	:param b: vector from linear system to solve
	:param eps: desired precision
	:param kmax: max number of iterations allowed
	"""
	n = a.shape[0]

	d = np.triu(np.tril(a))

	h, g = np.eye(n) - np.dot(inv(d), a), np.dot(inv(d), b)

	x0 = np.zeros(n)

	hl, hr = np.tril(h, -1), np.triu(h)

	h_seid = np.dot(inv(np.eye(n) - hl), hr)

	x, x_prev = np.zeros(n), x0

	for i in range(n):
		x[i] = sum(h[i, j] * x[j] for j in range(i)) + \
			sum(h[i, j] * x_prev[j] for j in range(i, n)) + g[i]

	iteration = 0
	while norm(h_seid) / (1 - norm(h_seid)) * norm(x - x_prev) >= eps and \
		iteration <= max_iterations:
		iteration += 1

		x_prev = np.copy(x)

		for i in range(n):
			x[i] = sum(h[i, j] * x[j] for j in range(i)) + \
				sum(h[i, j] * x_prev[j] for j in range(i, n)) + g[i]

		print(f'\nНа ітерації {iteration} маємо:\n'
			f'\tx = {x},\n'
			f'\tr = {np.dot(a, x) - b}\n\n')

	return x


def _a(i, j):
	"""
	:param i: row of entry of a to generate
	:param j: row of entry of a to generate
	"""
	if i != j:
		return (i + j - 1) / (2 * n)
	else:
		return n + 10 + (i + j - 1) / (2 * n)


if __name__ == '__main__':
	np.set_printoptions(linewidth=90)

	n = 6

	A = np.matrix([[_a(i, j) for j in range(1, n)] for i in range(1, n)])

	b = np.arange(17, 17 + 5 * (n - 1), 5)

	x_true = solve(A, b)

	x_seid = seidel(A, b, eps=1e-7)

	print(f"\nЗнайдений бібліотечною функцією розв'язок:\n"
		f"\tx = {x_true}\n\n")

	print(f"Знайдений нами розв'язок:\n"
		f"\tx = {x_seid}\n\n")

	print(f'Вектор нев\'язки:\n'
		f'\tr = {x_seid - x_true}\n')


__author__: "Nikita Skybytskyi"
__copyright__ = "Copyright 2019, KNU"
__credits__ = ["Nikita Skybytskyi"]
__license__ = "MIT"
__version__ = "1.1"
__maintainer__ = "Nikita Skybytskyi"
__email__ = "n.skybytskyi@knu.ua"
__status__ = "Production"
