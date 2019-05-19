#!/usr/bin/env python
from dashpot import Dashpot
from car import Car
from road import Road


class Stage:
    def __init__(self, car: Car, road: Road):
        self._car, self._road = car, road
        self._t = 0

    @property
    def car(self):
        return self._car
    
    @property
    def x(self):
        return self.car.x

    @property
    def dot_x(self):
        return self.car.dot_x

    @property
    def road(self):
        return self._road

    @property
    def t(self):
        return self._t
    
    @property
    def r(self) -> float:
        return self.car.r(self.road.dot_x_0(self.t))

    @property
    def xi(self) -> float:
        return self.car.xi(self.road.dot_x_0(self.t))

    @property
    def x_0(self) -> float:
        return self.road.x_0(self.t)

    @property
    def dot_x_0(self) -> float:
        return self.road.dot_x_0(self.t)

    def __repr__(self):
        return f'Stage(t={self.t:.7f}, car={self.car}, road={self.road})'

    def move(self, dt: float):
        def f(t: float, x: float, y: float) -> float:
            return y

        def g(t: float, x: float, y: float) -> float:
            return - 1 / self.car.m * (
                self.car.dashpot.k * (x - self.x_0) + self.r * (y - self.dot_x_0)
            )

        k1 = dt * f(self.t, self.x, self.dot_x)
        q1 = dt * g(self.t, self.x, self.dot_x)

        k2 = dt * f(self.t + dt / 2, self.x + k1 / 2, self.dot_x + q1 / 2)
        q2 = dt * g(self.t + dt / 2, self.x + k1 / 2, self.dot_x + q1 / 2)

        k3 = dt * f(self.t + dt / 2, self.x + k2 / 2, self.dot_x + q2 / 2)
        q3 = dt * g(self.t + dt / 2, self.x + k2 / 2, self.dot_x + q2 / 2)

        k4 = dt * f(self.t + dt, self.x + k3, self.dot_x + q3)
        q4 = dt * g(self.t + dt, self.x + k3, self.dot_x + q3)

        self._t, self.car._x, self.car._dot_x = self.t + dt, \
            self.x + (k1 + 2 * k2 + 2 * k3 + k4) / 6, \
            self.dot_x + (q1 + 2 * q2 + 2 * q3 + q4) / 6


if __name__ == '__main__':
    pass  # TODO(nsk): write tests and unittest main
