#!/usr/bin/env python
from math import cos, sin


class Road:
    def __init__(self, a: float, omega: float):
        assert a >= 0, "a must be positive"
        assert omega >= 0, "omega must be positive"
        self._a, self._omega = a, omega

    @property
    def a(self):
        return self._a

    @property
    def omega(self):
        return self._omega

    def __repr__(self):
        return f'Road(a={self.a}, omega={self.omega})'

    def x_0(self, t: float) -> float:
        return self.a * (1 - cos(self.omega * t))

    def dot_x_0(self, t: float) -> float:
        return self.a * self.omega * sin(self.omega * t)


if __name__ == '__main__':
    pass  # TODO(nsk): write tests and unittest main
