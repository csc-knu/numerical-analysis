import unittest

from nonlinear_equations import simple_iterate as si


class SimpleIterationTestCase(unittest.TestCase):
    def test_options_both_1_t(self):
        def f(x):
            return x ** 2 - 2

        with self.assertRaises(ValueError):
            si(lambda x: x**2 - 2, 0, 0, 2, options='-1 -t')

        with self.assertRaises(ValueError):
            si(lambda x: x ** 2 - 2, 0, 0, 2, options='-s -1 -t')

        with self.assertRaises(ValueError):
            si(lambda x: x**2 - 2, 0, 0, 2, options='-1 -s -t')

    def test_options_none_1_t(self):
        def f(x):
            return x ** 2 - 2

        with self.assertRaises(ValueError):
            si(f, 0, 0, 2)

        with self.assertRaises(ValueError):
            si(f, 0, 0, 2, options='-s')

        with self.assertRaises(ValueError):
            si(f, 0, 0, 2, options='-s -m')

    def test_options_s_a_le_b(self):
        def f(x):
            return x ** 2 - 2

        with self.assertRaises(ValueError):
            si(f, 0, 1, 1)

        with self.assertRaises(ValueError):
            si(f, 0, 1, 0)

        with self.assertRaises(ValueError):
            si(f, 0, 0, 0)

    def test_options_s_x_in_a_b(self):
        with self.assertRaises(ValueError):
            si(lambda x: x ** 2 - 2, 0, 1, 2)

        with self.assertRaises(ValueError):
            si(lambda x: x ** 2 - 2, -1, 0, 1)

        with self.assertRaises(ValueError):
            si(lambda x: x ** 2 - 2, 3, 0, 2)

    def test_options_1(self):
        self.assertEqual(True, False)

    def test_options_t(self):
        self.assertEqual(True, False)

    def test_eps(self):
        self.assertEqual(True, False)

if __name__ == '__main__':
    unittest.main()
