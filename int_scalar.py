#!/usr/bin/env python
import unittest
from typing import Callable


def integrate_left_rect(f: Callable[[float], float], a: float, b: float) -> float:
	return (b - a) * f(a)


def integrate_right_rect(f: Callable[[float], float], a: float, b: float) -> float:
	return (b - a) * f(b)


def integrate_mid_rect(f: Callable[[float], float], a: float, b: float) -> float:
	return (b - a) * f((a + b) / 2)


def integrate_trapezoid(f: Callable[[float], float], a: float, b: float) -> float:
	return (b - a) / 2 * (f(a) + f(b))


if __name__ == '__main__':
    unittest.main()
