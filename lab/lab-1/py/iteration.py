#!/usr/bin/env python
"""lab-1-chord.py: solves nonlinear equation f(x) = 0 
for x in [a, b] via iteration method."""
from math import sin


def simple_iterate(f, a, b, M1, x0, eps=1e-7, kmax=1e3):
	"""
	:param f: function to find root of
	:param a: left endpoint of interval to find root on
	:param b: right endpoint of interval to find root on
	:param M1: max |f'(x)| for x in [a, b]
	:param x0: starting point
	:param eps: desired precision
	:param kmax: max number of iterations allowed
	"""
	x, x_prev, i = x0, x0 + 2 * eps, 1
	
	def _converged():
		return abs(x - x_prev) < eps and f(x) < eps

	def _log():
		print(f'На ітерації {i} маємо:\n'
			f'\t x = {x},\n'
			f'\tΔx = {abs(x - x_prev)}\n')

	def phi(x):
		return x - (1 / M1) * f(x)

	def _next():
		nonlocal x, x_prev, i
		x, x_prev, i = phi(x), x, i + 1

	while not _converged() and i <= kmax:
		_next(), _log()

	return x


if __name__ == '__main__':
	def f(x: float) -> float:
		return x**2 - 20 * sin(x)

	a, b, M1, x0, x_star = 2, 3, 25.7998499320089, 2, 2.7529466338187049383

	print(f'\n"Справжній" розв\'язок x_star = {x_star}\n')

	x = simple_iterate(f, a, b, M1, x0)

	print(f"Знайдений нами розв'язок x = {x}\n")

	print(f"Похибка: {abs(x - x_star)}")


__author__: "Nikita Skybytskyi"
__copyright__ = "Copyright 2007, KNU"
__credits__ = ["Nikita Skybytskyi"]
__license__ = "MIT"
__version__ = "1.1.1"
__maintainer__ = "Nikita Skybytskyi"
__email__ = "n.skybytskyi@knu.ua"
__status__ = "Production"
