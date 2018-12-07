#!usr/bin/env python
import numpy as np
import unittest
from typing import Tuple


def lu_decompose(a: np.matrix) -> Tuple[np.matrix, np.matrix]:
	n = a.shape[0]

	L, U = np.zeros((n, n)), np.zeros((n, n))
	
	for i in range(n):
		for j in range(i, n):
			L[j, i] = a[j, i] - sum(L[j, k] * U[k, i] for k in range(i))
		for j in range(i, n):
			U[i, j] = (a[i, j] - sum(L[i, k] * U[k, j] for k in range(i))) / L[i, i]
	
	return L, U


def det(a: np.matrix) -> float:
	L, U = lu_decompose(a)
	return float(np.product(L.diagonal()))


if __name__ == '__main__':
	unittest.main()
