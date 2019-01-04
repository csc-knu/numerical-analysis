#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""chord.py: solves nonlinear equation f(x) = 0 
for x in [a, b] via chord method."""
from math import sin


def chord(f, a, b, m1, M1, x0, eps=1e-7, kmax=1e3):
	"""
	:param f: function to find root of
	:param a: left endpoint of interval to find root on
	:param b: right endpoint of interval to find root on
	:param m1: min |f'(x)| for x in [a, b]
	:param M1: max |f'(x)| for x in [a, b]
	:param x0: starting point
	:param eps: desired precision
	:param kmax: max number of iterations allowed
	"""
	def _converged():
		# nonlocal f, x, m1, eps, x_prev, M1, i, kmax
		return abs(f(x)) / m1 < eps and abs(x - x_prev) * (M1 - m1) / m1 < eps

	def _next():
		# nonlocal f, a, b, x, x_prev, i
		nonlocal x, x_prev, i
		if f(a) < 0 and f(b) > 0:
			x, x_prev, i = x - f(x) / (f(b) - f(x)) * (b - x), x, i + 1	
		if f(b) < 0 and f(a) > 0:
			x, x_prev, i = x - f(x) / (f(x) - f(a)) * (x - a), x, i + 1

	def _log():
		print(f'На ітерації {i} маємо:\n'
			f'\t x = {x},\n'
			f'\tΔx = {abs(x - x_prev)}\n')

	x, x_prev, i = x0, x0 + 2 * eps, 1

	while not _converged() and i <= kmax:
		_next(), _log()

	return x


if __name__ == '__main__':
	def f(x):
		return x**2 - 20 * sin(x)

	a, b, m1, M1, x0, x_star = 2, 3, 12.3229367309428, 25.7998499320089, 2, \
		2.7529466338187049383

	print(f'\n"Справжній" розв\'язок x_star = {x_star}\n')

	x = chord(f, a, b, m1, M1, x0)

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
