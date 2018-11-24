#!/usr/bin/env python
import numpy as np
import unittest
from math import inf, sqrt
from typing import Callable
from numpy.linalg import inv
from matrix_helder_norm import matrix_helder_norm
from matrix_operator_norm import matrix_operator_norm


def cond(a: np.matrix, norm: str or Callable[[np.matrix], float], 
	p: float or None=None) -> float:
	if isinstance(norm, str):
		if norm == 'helder':
			return matrix_helder_norm(a, p) * matrix_helder_norm(inv(a), p)
		if norm == 'operator':
			return matrix_operator_norm(a, p) * matrix_operator_norm(inv(a), p)
	else:
		return norm(inv(a)) * norm(a)


if __name__ == '__main__':
	unittest.main()
