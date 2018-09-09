import unittest

import math
from nonlinear_equations import divide_in_two as dit


class DivideInTwoTestCase(unittest.TestCase):
    def test_s_option(self):
        def f(x):
            return x**2 - 2
        a, b, ans = 2, 0, math.sqrt(2)
        for eps in [1e-3, 1e-5, 1e-7, 1e-9]:
            with self.assertRaises(ValueError):
                self.assertAlmostEqual(dit(f, a, b, eps, '-s'), ans, delta=eps)

    def test_no_s_option(self):
        def f(x):
            return x ** 2 - 2
        a, b = 2, 0
        for eps in [1e-3, 1e-5, 1e-7, 1e-9]:
            with self.assertRaises(ValueError):
                dit(f, a, b, eps, '')
        a, b = 1, -1
        for eps in [1e-3, 1e-5, 1e-7, 1e-9]:
            with self.assertRaises(ValueError):
                dit(f, a, b, eps, '')

    def test_m_option(self):
        self.assertEqual(True, False)

    def test_no_m_option(self):
        self.assertEqual(True, False)

    def test_endpoints_product(self):
        def f(x):
            return x ** 2
        a, b = 1, 2
        for eps in [1e-3, 1e-5, 1e-7, 1e-9]:
            with self.assertRaises(ValueError):
                dit(f, a, b, eps)
        a, b = -1, 1
        for eps in [1e-3, 1e-5, 1e-7, 1e-9]:
            with self.assertRaises(ValueError):
                dit(f, a, b, eps)

    def test_step_non_locals(self):
        self.assertEqual(True, False)

    def test_step_logs(self):
        self.assertEqual(True, False)

    def test_step_left(self):
        self.assertEqual(True, False)

    def test_step_right(self):
        self.assertEqual(True, False)

    def test_i_option(self):
        self.assertEqual(True, False)

    def test_no_i_option(self):
        self.assertEqual(True, False)

    def test_epsilon(self):
        for delta_exp in range(-2, -11, -1):
            self.assertAlmostEqual(dit(lambda x: x - math.pi, 0, 5, 10**delta_exp), math.pi, delta=10**delta_exp)

    def test_square_root(self):
        def f(x):
            return x**2 - 2
        a, b = 0, 2
        ans = math.sqrt(2)
        for eps in [1e-3, 1e-5, 1e-7, 1e-9]:
            self.assertAlmostEqual(dit(f, a, b, eps), ans, delta=eps)

    def test_qubic_root(self):
        def f(x):
            return x**3 - 2
        a, b, ans = 0, 2, 2 ** (1/3)
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
