#!/usr/bin/env python
import numpy as np
import unittest
from typing import Tuple
from math import exp, e


def diff_forward_h_vec(f: np.array, x: np.array) -> Tuple[np.array, np.array]:
    return x[:-1], (f[1:] - f[:-1]) / (x[1] - x[0])


def diff_backward_h_vec(f: np.array, x: np.array) -> Tuple[np.array, np.array]:
    return x[1:], (f[1:] - f[:-1]) / (x[1] - x[0])


def diff_symmetric_h_vec(f: np.array, x: np.array) -> Tuple[np.array, np.array]:
    return x[1:-1], (f[2:] - f[:-2]) / (2 * (x[1] - x[0]))


def diff_forward_h2_vec(f: np.array, x: np.array) -> Tuple[np.array, np.array]:
    return x[:-2], (-3 * f[:-2] + 4 * f[1:-1] - f[2:]) / (2 * (x[1] - x[0]))


def diff_backward_h2_vec(f: np.array, x: np.array) -> Tuple[np.array, np.array]:
    return x[2:], (3 * f[2:] - 4 * f[1:-1] + f[:-2]) / (2 * (x[1] - x[0]))


def diff_2_vec(f: np.array, x: np.array) -> Tuple[np.array, np.array]:
    return x[1:-1], (f[2:] - 2 * f[1:-1] + f[:-2]) / h**2



if __name__ == '__main__':
    unittest.main()
