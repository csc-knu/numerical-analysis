import math
from nonlinear_equations import divide_in_two as dit
import unittest


class DivideInTwoTestCase(unittest.TestCase):
    def test_s_option(self):
        def f(x):
            return x**2 - 2
        a, b, ans = 2, 0, math.sqrt(2)
        self.assertAlmostEqual(dit(f, a, b, 1e-3, '-s'), ans, delta=1e-3)
        self.assertAlmostEqual(dit(f, a, b, 1e-5, '-s'), ans, delta=1e-5)
        self.assertAlmostEqual(dit(f, a, b, 1e-7, '-s'), ans, delta=1e-7)

    def test_square_root(self):
        def f(x):
            return x**2 - 2
        a, b = 0, 2
        ans = math.sqrt(2)
        self.assertAlmostEqual(dit(f, a, b, 1e-3), ans, delta=1e-3)
        self.assertAlmostEqual(dit(f, a, b, 1e-5), ans, delta=1e-5)
        self.assertAlmostEqual(dit(f, a, b, 1e-7), ans, delta=1e-7)

    def test_qubic_root(self):
        def f(x):
            return x**3 - 2
        a, b, ans = 0, 2, 2 ** (1/3)
        self.assertAlmostEqual(dit(f, a, b, 1e-3), ans, delta=1e-3)
        self.assertAlmostEqual(dit(f, a, b, 1e-5), ans, delta=1e-5)
        self.assertAlmostEqual(dit(f, a, b, 1e-7), ans, delta=1e-7)

    def test_epsilon(self):
        for delta_exp in range(-2, -11, -1):
            self.assertAlmostEqual(dit(lambda x: x - math.pi, 0, 5, 10**delta_exp), math.pi, delta=10**delta_exp)


if __name__ == '__main__':
    unittest.main()
