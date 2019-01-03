#!/usr/bin/env python
from math import sin
from typing import Callable
import unittest


def chord(f: Callable[[float], float], a: float, b: float, m1: float, M1: float, x0: float, 
	eps: float=1e-7, kmax: int=1e3) -> float:
	x, x_prev, i = x0, x0 + 2 * eps, 1
	
	if f(a) < 0 and f(b) > 0:
		while abs(f(x)) / m1 >= eps and abs(x - x_prev) * (M1 - m1) / m1 >= eps and i <= kmax:
			print(f'На ітерації {i} маємо:\n'
				f'\tx = {x},\n'
				f'\tDelta x = {abs(x - x_prev)}\n')
			x, x_prev, i = x - f(x) / (f(b) - f(x)) * (b - x), x, i + 1

	if f(b) < 0 and f(a) > 0:
		while abs(f(x)) / m1 >= eps and abs(x - x_prev) * (M1 - m1) / m1 >= eps and i <= kmax:
			print(f'На ітерації {i} маємо:\n'
				f'\tx = {x},\n'
				f'\tDelta x = {abs(x - x_prev)}\n')
			x, x_prev, i = x - f(x) / (f(x) - f(a)) * (x - a), x, i + 1


	print(f'На ітерації {i} маємо:\n'
		f'\tx = {x},\n'
		f'\tDelta x = {abs(x - x_prev)}\n')

	return x


class TestChord(unittest.TestCase):
	def test_0(self):
		def f(x: float) -> float:
			return x**2 - 20 * sin(x)

		a, b, m1, M1, x0, x_star = 2, 3, 12.3229367309428, 25.7998499320089, 2, \
			2.7529466338187049383

		print(f'"Справжній" розв\'язок x_star = {x_star}\n')

		x = chord(f, a, b, m1, M1, x0)

		print(f"Знайдений нами розв'язок x = {x}\n")

		print(f"Похибка: {abs(x - x_star)}")

		self.assertAlmostEqual(x, x_star)


if __name__ == '__main__':
	unittest.main()
