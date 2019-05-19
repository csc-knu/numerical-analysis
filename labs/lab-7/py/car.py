#!/usr/bin/env python
from dashpot import Dashpot


class Car:
    def __init__(self, m: float, dashpot: Dashpot):
        assert m > 0, "m must be positive"
        self._m, self._dashpot = m, dashpot
        self._x, self._dot_x = 0, 0

    @property
    def m(self):
        return self._m
    
    @property
    def dashpot(self):
        return self._dashpot
    
    @property
    def x(self):
        return self._x
    
    @property
    def dot_x(self):
        return self._dot_x

    def __repr__(self):
        return f'Car(x={self.x:.7f}, dot_x={self.dot_x:.7f}, ' + \
            f'm={self.m}, dashpot={self.dashpot})'

    def r(self, dot_x_0: float) -> float:
        return self.dashpot.r(self.dot_x, dot_x_0)

    def xi(self, dot_x_0: float) -> float:
        return self.dashpot.xi(self.dot_x, dot_x_0, self.m)


if __name__ == '__main__':
    pass  # TODO(nsk): write tests and unittest main
