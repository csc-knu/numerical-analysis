# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 16:25:51 2018

@author: Nikita Skybytskyi

Solving Linear Systems of Algebraic Equations
"""

import numpy as np


def gauss(a: np.matrix, b: np.array) -> np.array:
    """
    :param a: matrix
    :param b: vector
    :return: solution-vector x
    """
    eps = 1e-7

    if a.shape[0] != a.shape[1]:
        raise ValueError(f'Dimensions mismatch: a.rows = {a.shape[0]} != {a.shape[1]} = a.cols')

    if b.shape[0] != a.shape[0]:
        raise ValueError(f'Dimensions mismatch: a.rows = {a.shape[0]} != {b.shape[0]} = b.rows')

    n = a.shape[0]
    
    p = list(range(n))

    for k in range(n):
        if abs(a[k, k]) < eps:
            for m in range(k + 1, n):
                if abs(a[k, m]) >= eps:
                    a[:, [k, m]] = a[:, [m, k]]
                    p[k], p[m] = p[m], p[k]
                    break

        b[k] /= a[k, k]
        a[k] /= a[k, k]

        for i in range(k + 1, n):
            b[i] -= a[i, k] * b[k]
            a[i] -= a[i, k] * a[k]

    x = b

    for i in range(n - 1, -1, -1):
        x[i] -= sum(a[i, j] * x[j] for j in range(i + 1, n))

    return np.array([x[p[i]] for i in range(n)])
