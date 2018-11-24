#!/usr/bin/env python
import unittest


def interpolation_error(method: str, M_d_plus_1: float, a: float or None=None, 
	b: float or None=None,n: int or None=None, d: int or None=None):
	if a is None:
		a = b - h * n
	if b is None:
		b = a + h * n
	if h is None:
		h = (b - a) / n
	if n is None:
		n = (b - a) / h

	dc = {
		'left rect': (0, 1 / 2),
		'right rect': (0, 1 / 2),
		'mid rect': (1, 1 / 24),
		'trapezoid': (1, 1 / 12),
		'simpson': (3, 1 / 2880),
	}

	d, c = dc[method]

	return c * (b - a) * ((b - a) / n)**(d + 1) * M_d_plus_1


if __name__ == '__main__':
    unittest.main()
