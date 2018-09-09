import unittest
import math

from nonlinear_equations import divide_in_two as dit, simple_iterate as si, \
    relaxate as r, newton as n, modified_newton as mn, secant as s


class DivideInTwoTestCase(unittest.TestCase):
    def test_quadratic(self):
        def f(x):
            return x**2 - 2
        a, b, ans = 0, 2, math.sqrt(2)
        for eps in [1e-3, 1e-5, 1e-7, 1e-9]:
            self.assertAlmostEqual(dit(f, a, b, eps), ans, delta=eps)

    def test_qubic(self):
        def f(x):
            return x**3 - 2
        a, b, ans = 0, 2, 2 ** (1/3)
        for eps in [1e-3, 1e-5, 1e-7, 1e-9]:
            self.assertAlmostEqual(dit(f, a, b, eps), ans, delta=eps)

    def test_sin(self):
        def f(x):
            return math.sin(x)
        a, b, ans = 3, 4, math.pi
        for eps in [1e-3, 1e-5, 1e-7, 1e-9]:
            self.assertAlmostEqual(dit(f, a, b, eps), ans, delta=eps)

    def test_cos(self):
        def f(x):
            return math.cos(x)
        a, b, ans = 0, 2, math.pi / 2
        for eps in [1e-3, 1e-5, 1e-7, 1e-9]:
            self.assertAlmostEqual(dit(f, a, b, eps), ans, delta=eps)

    def test_lab(self):
        def f(x):
            return ...
        a, b = ..., ...
        eps = ...
        ans = ...
        self.assertAlmostEqual(dit(f, a, b, eps), ans, delta=eps)


if __name__ == '__main__':
    unittest.main()
