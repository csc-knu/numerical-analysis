#!/usr/bin/env python
import numpy as np
import unittest
from math import factorial


def interpolate_hermit(x: np.array, f: np.array, x_to: float) -> float:
    m = x.shape[0]
   
    r = np.vectorize(len)(f)

    _r = sum(r)

    idx = np.hstack((np.full(r[i], i) for i in range(m)))
    
    rr = [[f[i][0] for i in idx]]

    for i in range(_r - 1):
        rr.append([])
        for j in range(_r - 1 - i):
            if idx[j] == idx[j + i + 1]:
                rr[-1].append(f[idx[j]][i + 1] / factorial(i + 1))
            else:
                rr[-1].append((rr[-2][j + 1] - rr[-2][j]) / (x[idx[j + i + 1]] - x[idx[j]]))
        
    pnx = rr[_r - 1][0]

    for i in range(_r - 1)[::-1]:
        pnx = pnx * (x_to - x[idx[i]]) + rr[i][0]
        
    return pnx


class TestInterpolateHermit(unittest.TestCase):
    def test_0(self):
        x = np.array([-1, 0, 2])
        f = np.array([np.array([-17, 33]), np.array([-4, 3, -8]), np.array([10,])])
        x_to = 1
                
        self.assertEqual(interpolate_hermit(x, f, x_to), -3)


if __name__ == '__main__':
	unittest.main()
