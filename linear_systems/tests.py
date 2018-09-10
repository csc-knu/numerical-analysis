import unittest
import numpy as np

from linear_systems.main import gauss


class GaussTestCase(unittest.TestCase):
    def test_2_by_2(self):
        a = np.matrix([[1, 2], [3, 4]], dtype=float)
        b = np.array([1, 1], dtype=float)
        x = np.array([-1, 1], dtype=float)
        g = gauss(a, b)
        for i in range(2):
            self.assertAlmostEqual(g[i], x[i], delta=1e-7)

        a = np.matrix([[3, -2], [5, 1]], dtype=float)
        b = np.array([-6, 3], dtype=float)
        x = np.array([0, 3], dtype=float)
        g = gauss(a, b)
        for i in range(2):
            self.assertAlmostEqual(g[i], x[i], delta=1e-7)

        a = np.matrix([[5, 2], [2, 1]], dtype=float)
        b = np.array([7, 9], dtype=float)
        x = np.array([-11, 31], dtype=float)
        g = gauss(a, b)
        for i in range(2):
            self.assertAlmostEqual(g[i], x[i], delta=1e-7)

    def test_3_by_3(self):
        a = np.matrix([[2, 1, 1], [1, -1, 0], [3, -1, 2]], dtype=float)
        b = np.array([2, -2, 2], dtype=float)
        x = np.array([-1, 1, 3], dtype=float)
        g = gauss(a, b)
        for i in range(3):
            self.assertAlmostEqual(g[i], x[i], delta=1e-7)

        a = np.matrix([[1, 2, 3], [3, 5, 7], [1, 3, 4]], dtype=float)
        b = np.array([3, 0, 1], dtype=float)
        x = np.array([-4, -13, 11], dtype=float)
        g = gauss(a, b)
        for i in range(3):
            self.assertAlmostEqual(g[i], x[i], delta=1e-7)

        a = np.matrix([[1, 1, 1], [4, 2, 1], [9, 3, 1]], dtype=float)
        b = np.array([0, 1, 3], dtype=float)
        x = np.array([.5, -.5, 0], dtype=float)
        g = gauss(a, b)
        for i in range(3):
            self.assertAlmostEqual(g[i], x[i], delta=1e-7)

    def test_4_by_4(self):
        a = np.matrix([[1, -2, -1, 1], [1, -8, -2, -3], [2, 2, -1, 7], [1, 1, 2, 1]], dtype=float)
        b = np.array([1, -2, 7, 1], dtype=float)
        x = np.array([-2, -1, 1, 2], dtype=float)
        g = gauss(a, b)
        for i in range(4):
            self.assertAlmostEqual(g[i], x[i], delta=1e-7)

        a = np.matrix([[3, 3, 6, 3], [3, 1, 5, 1], [2, 1, 4, 2], [1, 3, 3, 2]], dtype=float)
        b = np.array([6, 2, 1, 6], dtype=float)
        x = np.array([3, 3, -2, 0], dtype=float)
        g = gauss(a, b)
        for i in range(4):
            self.assertAlmostEqual(g[i], x[i], delta=1e-7)

        a = np.matrix([[2, 2, -3, 3], [3, 2, -1, 1], [1, 1, -2, 2], [2, 4, -3, 2]], dtype=float)
        b = np.array([-3, -3, -1, -3], dtype=float)
        x = np.array([2, -5, -11, -10], dtype=float)
        g = gauss(a, b)
        for i in range(4):
            self.assertAlmostEqual(g[i], x[i], delta=1e-7)

    def test_5_by_5(self):
        a = np.matrix([[1, 1, 0, 0, 0], [1, 1, 1, 0, 0], [0, 1, 1, 1, 0], [0, 0, 1, 1, 1], [0, 0, 0, 1, 1]], dtype=float)
        b = np.array([1, 4, -3, 2, -1], dtype=float)
        x = np.array([2, -5, -11, -10], dtype=float)
        g = gauss(a, b)
        for i in range(5):
            self.assertAlmostEqual(g[i], x[i], delta=1e-7)


if __name__ == '__main__':
    unittest.main()
