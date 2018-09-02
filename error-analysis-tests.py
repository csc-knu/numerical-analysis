import unittest

from error_analysis import absolute_error as ae, absolute_error_answer_wrapper as aeaw


class TestAbsoluteError(unittest.TestCase):
    def test_const_add_const(self):
        s = '1 + 1'
        self.assertEqual(ae(s), '')

        s = '1 + 2'
        self.assertEqual(ae(s), '')

    def test_cons_add_var(self):
        s = '1 + x'
        self.assertEqual(ae(s), 'Δx')

        s = '1 + x_1'
        self.assertEqual(ae(s), 'Δx_1')

    def test_var_add_const(self):
        s = 'y + 1'
        self.assertEqual(ae(s), 'Δy')

        s = 'y_1 + 1'
        self.assertEqual(ae(s), 'Δy_1')

    def test_var_add_var(self):
        s = 'x + y'
        self.assertEqual(ae(s), 'Δx + Δy')

        s = 'y + x'
        self.assertEqual(ae(s), 'Δy + Δx')

    def test_const_sub_const(self):
        s = '1 - 1'
        self.assertEqual(ae(s), '')

        s = '1 - 2'
        self.assertEqual(ae(s), '')

    def test_cons_sub_var(self):
        s = '1 - x'
        self.assertEqual(ae(s), 'Δx')

        s = '1 - x_1'
        self.assertEqual(ae(s), 'Δx_1')

    def test_var_sub_const(self):
        s = 'y - 1'
        self.assertEqual(ae(s), 'Δy')

        s = 'y_1 - 1'
        self.assertEqual(ae(s), 'Δy_1')

    def test_var_sub_var(self):
        s = 'x - y'
        self.assertEqual(ae(s), 'Δx + Δy')

        s = 'y - x'
        self.assertEqual(ae(s), 'Δy + Δx')

    def test_const_mul_const(self):
        s = '1 * 1'
        self.assertEqual(ae(s), '')

        s = '1 * 2'
        self.assertEqual(ae(s), '')

    def test_cons_mul_var(self):
        s = '1 * x'
        self.assertEqual(ae(s), '(1) * (Δx)')

        s = '2 * x'
        self.assertEqual(ae(s), '(2) * (Δx)')

        s = '1 * x_1'
        self.assertEqual(ae(s), '(1) * (Δx_1)')

        s = '2 * x_1'
        self.assertEqual(ae(s), '(2) * (Δx_1)')

    def test_var_mul_const(self):
        s = 'y * 1'
        self.assertEqual(ae(s), '(1) * (Δy)')

        s = 'y * 2'
        self.assertEqual(ae(s), '(2) * (Δy)')

        s = 'y_1 * 1'
        self.assertEqual(ae(s), '(1) * (Δy_1)')

        s = 'y_1 * 2'
        self.assertEqual(ae(s), '(2) * (Δy_1)')

    def test_var_mul_var(self):
        s = 'x * y'
        self.assertEqual(ae(s), '(x) * (Δy) + (y) * (Δx)')

        s = 'y * x'
        self.assertEqual(ae(s), '(y) * (Δx) + (x) * (Δy)')

    def test_const_div_const(self):
        s = '1 / 2'
        self.assertEqual(ae(s), '')

        s = '2 / 1'
        self.assertEqual(ae(s), '')

    def test_const_div_var(self):
        s = '1 / x'
        self.assertEqual(ae(s), '((1) * (Δx)) / (x)^2')

        s = '2 / y'
        self.assertEqual(ae(s), '((2) * (Δy)) / (y)^2')

    def test_var_div_const(self):
        s = 'x / 2'
        self.assertEqual(ae(s), '((2) * (Δx)) / (2)^2')

        s = 'y / 1'
        self.assertEqual(ae(s), '((1) * (Δy)) / (1)^2')

    def test_var_div_var(self):
        s = 'x / y'
        self.assertEqual(ae(s), '((x) * (Δy) + (y) * (Δx)) / (y)^2')

        s = 'y / x'
        self.assertEqual(ae(s), '((y) * (Δx) + (x) * (Δy)) / (x)^2')
        pass

    def test_wrong_symbols(self):
        s = '[1 + 2]'
        with self.assertRaises(ValueError):
            ae(s)

        s = '1 ^ 2'
        with self.assertRaises(ValueError):
            ae(s)

    def test_mul_div_wrong_args(self):
        s = '* 1'
        with self.assertRaises(ValueError):
            ae(s)

        s = '/ 1'
        with self.assertRaises(ValueError):
            ae(s)

    def test_wrong_parenthesises(self):
        s = '(1 + 2 * 3'
        with self.assertRaises(ValueError):
            ae(s)

        s = '1 + 2 * 3)'
        with self.assertRaises(ValueError):
            ae(s)

    def test_parenthesises_add(self):
        s = '(1 + 2) + 3'
        self.assertEqual(ae(s), '')

        s = '(1 + 2) + x'
        self.assertEqual(ae(s), 'Δx')

        s = '(1 + y) + x'
        self.assertEqual(ae(s), 'Δy + Δx')

    def test_parenthesises_sub(self):
        s = '(1 + 2) - 3'
        self.assertEqual(ae(s), '')

        s = '(1 + 2) - x'
        self.assertEqual(ae(s), 'Δx')

        s = '(1 + y) - x'
        self.assertEqual(ae(s), 'Δy + Δx')

    def test_parenthesises_mul(self):
        s = '(1 + 2) * 3'
        self.assertEqual(ae(s), '')

        s = '(1 + 2) * x'
        self.assertEqual(ae(s), '((1+2)) * (Δx)')

        s = '(1 + y) * x'
        self.assertEqual(ae(s), '((1+y)) * (Δx) + (x) * (Δy)')

        s = '(1 + y) * (x + 2)'
        self.assertEqual(ae(s), '((1+y)) * (Δx) + ((x+2)) * (Δy)')

    def test_parenthesises_div(self):
        s = '(1 + 2) / 3'
        self.assertEqual(ae(s), '')

        s = '(1 + 2) / x'
        self.assertEqual(ae(s), '(((1+2)) * (Δx)) / (x)^2')

        s = '(1 + y) / x'
        self.assertEqual(ae(s), '(((1+y)) * (Δx) + (x) * (Δy)) / (x)^2')

        s = '(1 + y) / (x + 2)'
        self.assertEqual(ae(s), '(((1+y)) * (Δx) + ((x+2)) * (Δy)) / ((x+2))^2')

    def test_custom(self):
        s = ''
        with self.assertRaises(IndexError):
            ae(s)


class TestAbsoluteErrorAnswerWrapper(unittest.TestCase):
    def test_const_add_const(self):
        s = '1 + 1'
        self.assertEqual(aeaw(s), '')

        s = '1 + 2'
        self.assertEqual(aeaw(s), '')

    def test_cons_add_var(self):
        s = '1 + x'
        self.assertEqual(aeaw(s), 'Δx')

        s = '1 + x_1'
        self.assertEqual(aeaw(s), 'Δx_1')

    def test_var_add_const(self):
        s = 'y + 1'
        self.assertEqual(aeaw(s), 'Δy')

        s = 'y_1 + 1'
        self.assertEqual(aeaw(s), 'Δy_1')

    def test_var_add_var(self):
        s = 'x + y'
        self.assertEqual(aeaw(s), 'Δx + Δy')

        s = 'y + x'
        self.assertEqual(aeaw(s), 'Δy + Δx')

    def test_const_sub_const(self):
        s = '1 - 1'
        self.assertEqual(aeaw(s), '')

        s = '1 - 2'
        self.assertEqual(aeaw(s), '')

    def test_cons_sub_var(self):
        s = '1 - x'
        self.assertEqual(aeaw(s), 'Δx')

        s = '1 - x_1'
        self.assertEqual(aeaw(s), 'Δx_1')

    def test_var_sub_const(self):
        s = 'y - 1'
        self.assertEqual(aeaw(s), 'Δy')

        s = 'y_1 - 1'
        self.assertEqual(aeaw(s), 'Δy_1')

    def test_var_sub_var(self):
        s = 'x - y'
        self.assertEqual(aeaw(s), 'Δx + Δy')

        s = 'y - x'
        self.assertEqual(aeaw(s), 'Δy + Δx')

    def test_const_mul_const(self):
        s = '1 * 1'
        self.assertEqual(aeaw(s), '')

        s = '1 * 2'
        self.assertEqual(aeaw(s), '')

    def test_cons_mul_var(self):
        s = '1 * x'
        self.assertEqual(aeaw(s), '(1) * (Δx)')

        s = '2 * x'
        self.assertEqual(aeaw(s), '(2) * (Δx)')

        s = '1 * x_1'
        self.assertEqual(aeaw(s), '(1) * (Δx_1)')

        s = '2 * x_1'
        self.assertEqual(aeaw(s), '(2) * (Δx_1)')

    def test_var_mul_const(self):
        s = 'y * 1'
        self.assertEqual(aeaw(s), '(1) * (Δy)')

        s = 'y * 2'
        self.assertEqual(aeaw(s), '(2) * (Δy)')

        s = 'y_1 * 1'
        self.assertEqual(aeaw(s), '(1) * (Δy_1)')

        s = 'y_1 * 2'
        self.assertEqual(aeaw(s), '(2) * (Δy_1)')

    def test_var_mul_var(self):
        s = 'x * y'
        self.assertEqual(aeaw(s), '(x) * (Δy) + (y) * (Δx)')

        s = 'y * x'
        self.assertEqual(aeaw(s), '(y) * (Δx) + (x) * (Δy)')

    def test_const_div_const(self):
        s = '1 / 2'
        self.assertEqual(aeaw(s), '')

        s = '2 / 1'
        self.assertEqual(aeaw(s), '')

    def test_const_div_var(self):
        s = '1 / x'
        self.assertEqual(aeaw(s), '((1) * (Δx)) / (x)^2')

        s = '2 / y'
        self.assertEqual(aeaw(s), '((2) * (Δy)) / (y)^2')

    def test_var_div_const(self):
        s = 'x / 2'
        self.assertEqual(aeaw(s), '((2) * (Δx)) / (2)^2')

        s = 'y / 1'
        self.assertEqual(aeaw(s), '((1) * (Δy)) / (1)^2')

    def test_var_div_var(self):
        s = 'x / y'
        self.assertEqual(aeaw(s), '((x) * (Δy) + (y) * (Δx)) / (y)^2')

        s = 'y / x'
        self.assertEqual(aeaw(s), '((y) * (Δx) + (x) * (Δy)) / (x)^2')
        pass

    def test_wrong_symbols(self):
        s = '[1 + 2]'
        with self.assertRaises(ValueError):
            aeaw(s)

        s = '1 ^ 2'
        with self.assertRaises(ValueError):
            aeaw(s)

    def test_mul_div_wrong_args(self):
        s = '* 1'
        with self.assertRaises(ValueError):
            aeaw(s)

        s = '/ 1'
        with self.assertRaises(ValueError):
            aeaw(s)

    def test_wrong_parenthesises(self):
        s = '(1 + 2 * 3'
        with self.assertRaises(ValueError):
            aeaw(s)

        s = '1 + 2 * 3)'
        with self.assertRaises(ValueError):
            aeaw(s)

    def test_parenthesises_add(self):
        s = '(1 + 2) + 3'
        self.assertEqual(aeaw(s), '')

        s = '(1 + 2) + x'
        self.assertEqual(aeaw(s), 'Δx')

        s = '(1 + y) + x'
        self.assertEqual(aeaw(s), 'Δy + Δx')

    def test_parenthesises_sub(self):
        s = '(1 + 2) - 3'
        self.assertEqual(aeaw(s), '')

        s = '(1 + 2) - x'
        self.assertEqual(aeaw(s), 'Δx')

        s = '(1 + y) - x'
        self.assertEqual(aeaw(s), 'Δy + Δx')

    def test_parenthesises_mul(self):
        s = '(1 + 2) * 3'
        self.assertEqual(aeaw(s), '')

        s = '(1 + 2) * x'
        self.assertEqual(aeaw(s), '(1 + 2) * (Δx)')

        s = '(1 + y) * x'
        self.assertEqual(aeaw(s), '(1 + y) * (Δx) + (x) * (Δy)')

        s = '(1 + y) * (x + 2)'
        self.assertEqual(aeaw(s), '(1 + y) * (Δx) + (x + 2) * (Δy)')

    def test_parenthesises_div(self):
        s = '(1 + 2) / 3'
        self.assertEqual(aeaw(s), '')

        s = '(1 + 2) / x'
        self.assertEqual(aeaw(s), '((1 + 2) * (Δx)) / (x)^2')

        s = '(1 + y) / x'
        self.assertEqual(aeaw(s), '((1 + y) * (Δx) + (x) * (Δy)) / (x)^2')

        s = '(1 + y) / (x + 2)'
        self.assertEqual(aeaw(s), '((1 + y) * (Δx) + (x + 2) * (Δy)) / (x + 2)^2')

    def test_custom(self):
        s = ''
        with self.assertRaises(IndexError):
            aeaw(s)


if __name__ == '__main__':
    unittest.main()
