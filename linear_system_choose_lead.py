#!/usr/bin/env python
import numpy as np
import unittest
from math import sin, cos


def linear_system_gauss_choose_colmax(a: np.matrix) -> np.array:
	n = a.shape[0]

	for k in range(n):
		colmax = np.max(a[k:, k])

		for j in range(k, n):
			if a[j, k] == colmax:
				a[k], a[j] = a[j], a[k]
				break

		a[k] /= a[k, k]
		for j in range(k + 1, n):
			a[j] -= a[k] * a[j, k]
	
	x = np.zeros(n)

	for i in range(n)[::-1]:
		x[i] = a[i, n] - sum(a[i, j] * x[j] for j in range(i + 1, n))

	return x


def linear_system_gauss_choose_rowmax(a: np.matrix) -> np.array:
	n = a.shape[0]

	p = np.arange(n)

	for k in range(n): 
		rowmax = np.max(a[k, k:n])

		for j in range(k, n):
			if a[k, j] == rowmax:
				a[:, k], a[:, j] = a[:, j], a[:, k]
				p[k], p[j] = p[j], p[k]
				break

		a[k] /= a[k, k]
		for j in range(k + 1, n):
			a[j] -= a[k] * a[j, k]
	
	x = np.zeros(n)

	for i in range(n)[::-1]:
		x[i] = a[i, n] - sum(a[i, j] * x[j] for j in range(i + 1, n))

	return x[p]


def linear_system_jordan_choose_colmax(a: np.matrix) -> np.array:
	n = a.shape[0]

	for k in range(n):
		colmax = np.max(a[k:, k])

		for j in range(k, n):
			if a[j, k] == colmax:
				a[k], a[j] = a[j], a[k]
				break

		a[k] /= a[k, k]
		for j in range(n):
			if j != k:
				a[j] -= a[k] * a[j, k]
	
	return a[:, n]


def linear_system_jordan_choose_rowmax(a: np.matrix) -> np.array:
	n = a.shape[0]

	p = np.arange(n)

	for k in range(n): 
		rowmax = np.max(a[k, k:n])

		for j in range(k, n):
			if a[k, j] == rowmax:
				a[:, k], a[:, j] = a[:, j], a[:, k]
				p[k], p[j] = p[j], p[k]
				break

		a[k] /= a[k, k]
		for j in range(n):
			if j != k:
				a[j] -= a[k] * a[j, k]
	
	return a[:, n][p]


if __name__ == '__main__':
	unittest.main()
