#!/usr/bin/env python
""" implementation of a secant method of solving nonlinear equations with unittest """
from math import sin
from typing import Callable
import unittest


def secant(f: Callable[[float], float], x0: float, eps: float=1e-7, kmax: int=1e3) -> float:
	x, x_prev, i = x0, x0 + 2 * eps, 1
	
	while abs(x - x_prev) >= eps and i <= kmax:
		print(f'На ітерації {i} маємо:\n'
			f'\tx = {x},\n'
			f'\tDelta x = {abs(x - x_prev)}\n')
		x, x_prev, i = x - f(x) / (f(x) - f(x_prev)) * (x - x_prev), x, i + 1


	print(f'На ітерації {i} маємо:\n'
		f'\tx = {x},\n'
		f'\tDelta x = {abs(x - x_prev)}\n')

	return x


class TestSecant(unittest.TestCase):
	def test_0(self):
		def f(x: float) -> float:
			return x**2 - 20 * sin(x)


		x0, x_star = 2, 2.7529466338187049383

		print(f'"Справжній" розв\'язок x_star = {x_star}\n')

		x = secant(f, x0)

		print(f"Знайдений нами розв'язок x = {x}\n")

		print(f"Похибка: {abs(x - x_star)}")

		self.assertAlmostEqual(x, x_star)


if __name__ == '__main__':
	unittest.main()
