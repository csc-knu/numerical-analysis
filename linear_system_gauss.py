#!/usr/bin/env python
import numpy as np
import unittest
from math import sin, cos


def linear_system_gauss(a: np.matrix) -> np.array:
	n = a.shape[0]

	for k in range(n): 
		a[k] /= a[k, k]
		for j in range(k + 1, n):
			a[j] -= a[k] * a[j, k]
	
	x = np.zeros(n)

	for i in range(n)[::-1]:
		x[i] = a[i, n] - sum(a[i, j] * x[j] for j in range(i + 1, n))

	return x


def linear_system_jordan(a: np.matrix) -> np.array:
	n = a.shape[0]

	for k in range(n): 
		a[k] /= a[k, k]
		for j in range(n):
			if j != k:
				a[j] -= a[k] * a[j, k]
	
	return a[:, n]


if __name__ == '__main__':
	unittest.main()
