# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 11:04:45 2018

@author: Nikita Skybytskyi, OM-3

Solving Nonlinear Equations Unit Tests
"""

import unittest
import math

from nonlinear_equations.main import divide_in_two as dit, simple_iterate as sit, \
    relaxate as rel, newton as net, modified_newton as mne, secant as sec


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
            return x**4 - 4 * x**3 + 5.5 * x**2 - 3 * x + 0.5

        a, b, ans = 0, 0.7, 0.292893

        for eps in [1e-6]:
            self.assertAlmostEqual(dit(f, a, b, eps), ans, delta=eps)


class SimpleIterateTestCase(unittest.TestCase):
    def test_quadratic(self):
        def f(x):
            return x**2 - 2

        def tau(x):
            return -0.2 * x

        x0, a, b, ans = 1, 0, 2, math.sqrt(2)

        for eps in [1e-3, 1e-5, 1e-7, 1e-9]:
            self.assertAlmostEqual(sit(f, x0, a, b, eps, tau), ans, delta=eps)

    def test_qubic(self):
        def f(x):
            return x**3 - 2

        def tau(x):
            return -0.1 * x

        x0, a, b, ans = 1, 0, 2, 2 ** (1/3)

        for eps in [1e-3, 1e-5, 1e-7, 1e-9]:
            self.assertAlmostEqual(sit(f, x0, a, b, eps, tau), ans, delta=eps)

    def test_sin(self):
        def f(x):
            return math.sin(x)

        def tau(x):
            return 0.2 * x

        x0, a, b, ans = 3, 3, 4, math.pi

        for eps in [1e-3, 1e-5, 1e-7, 1e-9]:
            self.assertAlmostEqual(sit(f, x0, a, b, eps, tau), ans, delta=eps)

    def test_cos(self):
        def f(x):
            return math.cos(x)

        def tau(x):
            return x

        x0, a, b, ans = 1, 0, 2, math.pi / 2

        for eps in [1e-3, 1e-5, 1e-7, 1e-9]:
            self.assertAlmostEqual(sit(f, x0, a, b, eps, tau), ans, delta=eps)

    def test_lab(self):
        def f(x):
            return x**4 - 4 * x**3 + 5.5 * x**2 - 3 * x + 0.5

        x0, a, b, ans = 0.5, 0, 0.7, 0.292893

        for eps in [1e-6]:
            self.assertAlmostEqual(sit(f, x0, a, b, eps), ans, delta=eps)


class RelaxateTestCase(unittest.TestCase):
    def test_quadratic(self):
        def f(x):
            return x**2 - 2

        x0, a, b, ans, tau = 1, 1, 2, math.sqrt(2), -0.2

        for eps in [1e-3, 1e-5, 1e-7, 1e-9]:
            self.assertAlmostEqual(rel(f, x0, a, b, eps, tau), ans, delta=eps)

    def test_qubic(self):
        def f(x):
            return x**3 - 2

        x0, a, b, ans, tau = 2, 0, 2, 2 ** (1/3), -0.1

        for eps in [1e-3, 1e-5, 1e-7, 1e-9]:
            self.assertAlmostEqual(rel(f, x0, a, b, eps, tau), ans, delta=eps)

    def test_sin(self):
        def f(x):
            return math.sin(x)

        x0, a, b, ans = 3, 3, 4, math.pi

        for eps in [1e-3, 1e-5, 1e-7, 1e-9]:
            self.assertAlmostEqual(rel(f, x0, a, b, eps), ans, delta=eps)

    def test_cos(self):
        def f(x):
            return math.cos(x)

        x0, a, b, ans = 0, 0, 2, math.pi / 2

        for eps in [1e-3, 1e-5, 1e-7, 1e-9]:
            self.assertAlmostEqual(rel(f, x0, a, b, eps), ans, delta=eps)

    def test_lab(self):
        def f(x):
            return x**4 - 4 * x**3 + 5.5 * x**2 - 3 * x + 0.5

        x0, a, b, ans = 0.5, 0, 0.7, 0.292893

        for eps in [1e-6]:
            self.assertAlmostEqual(rel(f, x0, a, b, eps), ans, delta=eps)


class NewtonTestCase(unittest.TestCase):
    def test_quadratic(self):
        def f(x):
            return x**2 - 2

        def d(x):
            return 2 * x

        x0, a, b, ans = 1, 0, 2, math.sqrt(2)

        for eps in [1e-3, 1e-5, 1e-7, 1e-9]:
            self.assertAlmostEqual(net(f, d, x0, a, b, eps), ans, delta=eps)

    def test_qubic(self):
        def f(x):
            return x**3 - 2

        def d(x):
            return 3 * x**2

        x0, a, b, ans = 1, 0, 2, 2 ** (1/3)

        for eps in [1e-3, 1e-5, 1e-7, 1e-9]:
            self.assertAlmostEqual(net(f, d, x0, a, b, eps), ans, delta=eps)

    def test_sin(self):
        def f(x):
            return math.sin(x)

        def d(x):
            return math.cos(x)

        x0, a, b, ans = 4, 3, 4, math.pi

        for eps in [1e-3, 1e-5, 1e-7, 1e-9]:
            self.assertAlmostEqual(net(f, d, x0, a, b, eps), ans, delta=eps)

    def test_cos(self):
        def f(x):
            return math.cos(x)

        def d(x):
            return - math.sin(x)

        x0, a, b, ans = 0.01, 0, 2, math.pi / 2

        for eps in [1e-3, 1e-5, 1e-7, 1e-9]:
            self.assertAlmostEqual(net(f, d, x0, a, b, eps), ans, delta=eps)

    def test_lab(self):
        def f(x):
            return x**4 - 4 * x**3 + 5.5 * x**2 - 3 * x + 0.5

        def d(x):
            return 4 * x**3 - 12 * x**2 + 11 * x - 3

        x0, a, b, ans = 0.4, 0, 0.7, 0.292893

        for eps in [1e-6]:
            self.assertAlmostEqual(net(f, d, x0, a, b, eps), ans, delta=eps)


class ModifiedNewtonTestCase(unittest.TestCase):
    def test_quadratic(self):
        def f(x):
            return x**2 - 2

        dx0, x0, a, b, ans = 2, 1, 0, 2, math.sqrt(2)

        for eps in [1e-3, 1e-5, 1e-7, 1e-9]:
            self.assertAlmostEqual(mne(f, dx0, x0, a, b, eps), ans, delta=eps)

    def test_qubic(self):
        def f(x):
            return x**3 - 2

        dx0, x0, a, b, ans = 3, 1, 0, 2, 2 ** (1/3)

        for eps in [1e-3, 1e-5, 1e-7, 1e-9]:
            self.assertAlmostEqual(mne(f, dx0, x0, a, b, eps), ans, delta=eps)

    def test_sin(self):
        def f(x):
            return math.sin(x)

        dx0, x0, a, b, ans = math.cos(4), 4, 3, 4, math.pi

        for eps in [1e-3, 1e-5, 1e-7, 1e-9]:
            self.assertAlmostEqual(mne(f, dx0, x0, a, b, eps), ans, delta=eps)

    def test_cos(self):
        def f(x):
            return math.cos(x)

        dx0, x0, a, b, ans = -1, 0, 0, 2, math.pi / 2

        for eps in [1e-3, 1e-5, 1e-7, 1e-9]:
            self.assertAlmostEqual(mne(f, dx0, x0, a, b, eps), ans, delta=eps)

    def test_lab(self):
        def f(x):
            return x**4 - 4 * x**3 + 5.5 * x**2 - 3 * x + 0.5

        dx0, x0, a, b, ans = -0.762, 0.3, 0, 0.7, 0.292893

        for eps in [1e-6]:
            self.assertAlmostEqual(mne(f, dx0, x0, a, b, eps), ans, delta=eps)


class SecantTestCase(unittest.TestCase):
    def test_quadratic(self):
        def f(x):
            return x**2 - 2

        x0, x1, a, b, ans = 0.5, 1, 0, 2, math.sqrt(2)

        for eps in [1e-3, 1e-5, 1e-7, 1e-9]:
            self.assertAlmostEqual(sec(f, x0, x1, a, b, eps), ans, delta=eps)

    def test_qubic(self):
        def f(x):
            return x**3 - 2

        x0, x1, a, b, ans = 0, 1, 0, 2, 2 ** (1/3)

        for eps in [1e-3, 1e-5, 1e-7, 1e-9]:
            self.assertAlmostEqual(sec(f, x0, x1, a, b, eps), ans, delta=eps)

    def test_sin(self):
        def f(x):
            return math.sin(x)

        x0, x1, a, b, ans = 3, 4, 3, 4, math.pi

        for eps in [1e-3, 1e-5, 1e-7, 1e-9]:
            self.assertAlmostEqual(sec(f, x0, x1, a, b, eps), ans, delta=eps)

    def test_cos(self):
        def f(x):
            return math.cos(x)

        x0, x1, a, b, ans = 0.01, 1, 0, 2, math.pi / 2

        for eps in [1e-3, 1e-5, 1e-7, 1e-9]:
            self.assertAlmostEqual(sec(f, x0, x1, a, b, eps), ans, delta=eps)

    def test_lab(self):
        def f(x):
            return x**4 - 4 * x**3 + 5.5 * x**2 - 3 * x + 0.5

        x0, x1, a, b, ans = 0.5, 0.4, 0, 0.7, 0.292893

        for eps in [1e-6]:
            self.assertAlmostEqual(sec(f, x0, x1, a, b, eps), ans, delta=eps)


if __name__ == '__main__':
    unittest.main()
