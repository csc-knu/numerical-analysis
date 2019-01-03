#!usr/bin/env python
import numpy as np
import unittest
from numpy.linalg import inv, norm, solve


def seidel(a, b, eps, max_iterations=1e3):
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

		print(f'На ітерації {iteration} маємо:\n\tx = {x},\n\tr = {np.dot(a, x) - b}\n')

	return x


def a(i, j):
	if i != j:
		return (i + j - 1) / (2 * n)
	else:
		return n + 10 + (i + j - 1) / (2 * n)


n = 5

A = np.matrix([[a(i, j) for j in range(1, n + 1)] for i in range(1, n + 1)])

b = np.array([17, 22, 27, 32, 37])
x_true = solve(A, b)

print(f"\nЗнайдений бібліотечною функцією розв'язок:\n\t{x_true}\n")

x_seid = seidel(A, b, eps=1e-10)

print(f"Знайдений нами розв'язок:\n\t{x_seid}\n")

print(f'Вектор нев\'язки:\n\t{x_seid - x_true}\n')