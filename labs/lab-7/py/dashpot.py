#!/usr/bin/env python
from math import sqrt


class Dashpot:
    def __init__(self, k: float, r_0: float, c: float):
        assert r_0 > 0, "r_0 must be positive"
        assert k > 0, "k must be positive"
        self._k, self._r_0, self._c = k, r_0, c

    @property
    def k(self):
        return self._k
    
    @property
    def r_0(self):
        return self._r_0

    @property
    def c(self):
        return self._c

    def __repr__(self):
        return f'Dashpot(k={self.k}, r_0={self.r_0}, c={self.c})'

    def r(self, dot_x: float, dot_x_0: float) -> float:
        return self.r_0 * (1 + self.c * abs(dot_x - dot_x_0))

    def xi(self, r: float, m: float) -> float:
        return r / (2 * sqrt(self.k * m))

    def xi(self, dot_x: float, dot_x_0: float, m: float) -> float:
        return self.r(dot_x, dot_x_0) / (2 * sqrt(self.k * m))


if __name__ == '__main__':
    pass  # TODO(nsk): write tests and unittest main
