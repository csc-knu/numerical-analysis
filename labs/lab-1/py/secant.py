#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""secant.py: solves nonlinear equation f(x) = 0 
for x in [a, b] via secant method."""
from math import sin


def secant(f, x0, eps=1e-7, kmax=1e3):
	"""
	:param f: function to find root of
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

	def _next():
		nonlocal x, x_prev, i
		x, x_prev, i = x - f(x) / (f(x) - f(x_prev)) * (x - x_prev), x, i + 1

	while not _converged() and i <= kmax:
		_next(), _log()

	return x


if __name__ == '__main__':
	def f(x):
			return x**2 - 20 * sin(x)

	x0, x_star = 2, 2.7529466338187049383

	print(f'\n"Справжній" розв\'язок x_star = {x_star}\n')

	x = secant(f, x0)

	print(f"Знайдений нами розв'язок x = {x}\n")

	print(f"Похибка: {abs(x - x_star)}")


__author__: "Nikita Skybytskyi"
__copyright__ = "Copyright 2019, KNU"
__credits__ = ["Nikita Skybytskyi"]
__license__ = "MIT"
__version__ = "1.1.1"
__maintainer__ = "Nikita Skybytskyi"
__email__ = "n.skybytskyi@knu.ua"
__status__ = "Production"
