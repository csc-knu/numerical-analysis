import unittest
import math

from nonlinear_equations import divide_in_two as dit, simple_iterate as sit, \
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
        def f():
            return ...

        a, b, ans = ..., ..., ...

        for eps in [1e-3, 1e-5, 1e-7, 1e-9]:
            self.assertAlmostEqual(dit(f, a, b, eps), ans, delta=eps)


class SimpleIterateTestCase(unittest.TestCase):
    def test_quadratic(self):
        def f(x):
            return x**2 - 2

        a, b, ans = 0, 2, math.sqrt(2)

        for eps in [1e-3, 1e-5, 1e-7, 1e-9]:
            self.assertAlmostEqual(sit(f, a, b, eps), ans, delta=eps)

    def test_qubic(self):
        def f(x):
            return x**3 - 2

        a, b, ans = 0, 2, 2 ** (1/3)

        for eps in [1e-3, 1e-5, 1e-7, 1e-9]:
            self.assertAlmostEqual(sit(f, a, b, eps), ans, delta=eps)

    def test_sin(self):
        def f(x):
            return math.sin(x)

        a, b, ans = 3, 4, math.pi

        for eps in [1e-3, 1e-5, 1e-7, 1e-9]:
            self.assertAlmostEqual(sit(f, a, b, eps), ans, delta=eps)

    def test_cos(self):
        def f(x):
            return math.cos(x)

        a, b, ans = 0, 2, math.pi / 2

        for eps in [1e-3, 1e-5, 1e-7, 1e-9]:
            self.assertAlmostEqual(sit(f, a, b, eps), ans, delta=eps)

    def test_lab(self):
        def f():
            return ...

        a, b, ans = ..., ..., ...

        for eps in [1e-3, 1e-5, 1e-7, 1e-9]:
            self.assertAlmostEqual(sit(f, a, b, eps), ans, delta=eps)


class RelaxateTestCase(unittest.TestCase):
    def test_quadratic(self):
        def f(x):
            return x**2 - 2

        a, b, ans = 0, 2, math.sqrt(2)

        for eps in [1e-3, 1e-5, 1e-7, 1e-9]:
            self.assertAlmostEqual(rel(f, a, b, eps), ans, delta=eps)

    def test_qubic(self):
        def f(x):
            return x**3 - 2

        a, b, ans = 0, 2, 2 ** (1/3)

        for eps in [1e-3, 1e-5, 1e-7, 1e-9]:
            self.assertAlmostEqual(rel(f, a, b, eps), ans, delta=eps)

    def test_sin(self):
        def f(x):
            return math.sin(x)

        a, b, ans = 3, 4, math.pi

        for eps in [1e-3, 1e-5, 1e-7, 1e-9]:
            self.assertAlmostEqual(rel(f, a, b, eps), ans, delta=eps)

    def test_cos(self):
        def f(x):
            return math.cos(x)

        a, b, ans = 0, 2, math.pi / 2

        for eps in [1e-3, 1e-5, 1e-7, 1e-9]:
            self.assertAlmostEqual(rel(f, a, b, eps), ans, delta=eps)

    def test_lab(self):
        def f():
            return ...

        a, b, ans = ..., ..., ...

        for eps in [1e-3, 1e-5, 1e-7, 1e-9]:
            self.assertAlmostEqual(rel(f, a, b, eps), ans, delta=eps)


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

        x0, a, b, ans = 0, 0, 2, math.pi / 2

        for eps in [1e-3, 1e-5, 1e-7, 1e-9]:
            self.assertAlmostEqual(net(f, d, x0, a, b, eps), ans, delta=eps)

    def test_lab(self):
        def f():
            return ...

        def d():
            return ...

        x0, a, b, ans = ..., ..., ..., ...

        for eps in [1e-3, 1e-5, 1e-7, 1e-9]:
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
        def f():
            return ...

        dx0, x0, a, b, ans = ..., ..., ..., ..., ...

        for eps in [1e-3, 1e-5, 1e-7, 1e-9]:
            self.assertAlmostEqual(mne(f, dx0, x0, a, b, eps), ans, delta=eps)


class SecantTestCase(unittest.TestCase):
    def test_quadratic(self):
        def f(x):
            return x**2 - 2

        x0, x1, a, b, ans = 0, 1, 0, 2, math.sqrt(2)

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

        x0, x1, a, b, ans = 0, 1, 0, 2, math.pi / 2

        for eps in [1e-3, 1e-5, 1e-7, 1e-9]:
            self.assertAlmostEqual(sec(f, x0, x1, a, b, eps), ans, delta=eps)

    def test_lab(self):
        def f():
            return ...

        x0, x1, a, b, ans = ..., ..., ..., ..., ...

        for eps in [1e-3, 1e-5, 1e-7, 1e-9]:
            self.assertAlmostEqual(rel(f, a, b, eps), ans, delta=eps)


if __name__ == '__main__':
    unittest.main()
