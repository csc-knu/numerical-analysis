#!/usr/bin/env python
import unittest
from typing import Callable
from math import exp, e


def diff_forward_h(f: Callable[[float], float], x: float, h: float) -> float:
    return (f(x + h) - f(x)) / h


def diff_backward_h(f: Callable[[float], float], x: float, h: float) -> float:
    return (f(x) - f(x - h)) / h


def diff_symmetric_h(f: Callable[[float], float], x: float, h: float) -> float:
    return (f(x + h) - f(x - h)) / (2 * h)


def diff_forward_h2(f: Callable[[float], float], x: float, h: float) -> float:
    return (-3 * f(x) + 4 * f(x + h) - f(x + 2 * h)) / (2 * h)


def diff_backward_h2(f: Callable[[float], float], x: float, h: float) -> float:
    return (3 * f(x) - 4 * f(x - h) + f(x - 2 * h)) / (2 * h)


def diff_2(f: Callable[[float], float], x: float, h: float) -> float:
    return (f(x + h) - 2 * f(x) + f(x - h)) / h**2


class TestDifferentiateAnalytical(unittest.TestCase):
    def test_diff_forward_h_0(self):
        def f(x: float) -> float:
            return exp(2 * x)

        x, h = 1, 1e-8

        self.assertAlmostEqual(diff_forward_h(f, x, h), 2 * e**2)


    def test_diff_backward_h_0(self):
        def f(x: float) -> float:
            return exp(2 * x)

        x, h = 1, 1e-8

        self.assertAlmostEqual(diff_backward_h(f, x, h), 2 * e**2)


    def test_diff_symmetric_h_0(self):
        def f(x: float) -> float:
            return exp(2 * x)

        x, h = 1, 1e-5

        self.assertAlmostEqual(diff_symmetric_h(f, x, h), 2 * e**2)


    def test_diff_forward_h2_0(self):
        def f(x: float) -> float:
            return exp(2 * x)

        x, h = 1, 1e-5

        self.assertAlmostEqual(diff_forward_h2(f, x, h), 2 * e**2)


    def test_diff_backward_h2_0(self):
        def f(x: float) -> float:
            return exp(2 * x)

        x, h = 1, 1e-5

        self.assertAlmostEqual(diff_backward_h2(f, x, h), 2 * e**2)


    def test_diff_2_0(self):
        def f(x: float) -> float:
            return exp(2 * x)

        x, h = 1, 1e-4

        self.assertAlmostEqual(diff_2(f, x, h), 4 * e**2)


if __name__ == '__main__':
    unittest.main()
