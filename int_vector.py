#!/usr/bin/env python
import unittest
from typing import Callable


def integrate_left_rect_vec(f: Callable[[float], float], a: float or None=None, 
	b: float or None=None, h: float or None=None, n: int or None=None) -> float:
	if a is None:
		a = b - h * n
	if b is None:
		b = a + h * n
	if h is None:
		h = (b - a) / n
	if n is None:
		n = (b - a) / h
	return h * sum(f(a + k * h) for k in range(n))


def integrate_right_rect_vec(f: Callable[[float], float], a: float or None=None, 
	b: float or None=None, h: float or None=None, n: int or None=None) -> float:
	if a is None:
		a = b - h * n
	if b is None:
		b = a + h * n
	if h is None:
		h = (b - a) / n
	if n is None:
		n = (b - a) / h
	return h * sum(f(b - k * h) for k in range(n))


def integrate_mid_rect_vec(f: Callable[[float], float], a: float or None=None, 
	b: float or None=None, h: float or None=None, n: int or None=None) -> float:
	if a is None:
		a = b - h * n
	if b is None:
		b = a + h * n
	if h is None:
		h = (b - a) / n
	if n is None:
		n = (b - a) / h
	return h * sum(f(a + k * h + h / 2) for k in range(n))


if __name__ == '__main__':
    unittest.main()
