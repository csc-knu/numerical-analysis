#!/usr/bin/env python
import numpy as np
import unittest
import matplotlib.pyplot as plt
from typing import Callable, List


def interpolate_newton_equidistant(y: List[float], a: float or None=None, 
	b: float or None=None, n: int or None=None, h: float or None=None) -> None:
	"""
	:param y: tables of values
	:param a: left endpoint
	:param b: right endpoint
	:param n: number of points
	:param h: step
	:return: P_n, as a list of coefficients
	"""
	if a is None:
		a = b - h * (n - 1)
	if b is None:
		b = a + h * (n - 1)
	if n is None:
		n = int((b - a) / h + 1)
	if h is None:
		h = (b - a) / (n - 1)

	x = [a + i * h for i in range(n)]

	_round = 9

	print(
		f'Вузли інтерполяції:\n'
		f'\t{list(map(lambda _: round(_, _round), x))}\n'
	)

	rr = [x, [(y[i] - y[i + 1]) / (x[i] - x[i + 1]) for i in range(n - 1)]]

	print(
		f'Значення функції у вузлах:\n'
		f'\t{list(map(lambda _: round(_, _round), y))}\n'
	)	

	print(
		f'Розділені різниці 1-го порядку:\n'
		f'\t{list(map(lambda _: round(_, _round), rr[1]))}\n'
	)

	for i in range(2, n):
		rr.append([0 for _ in range(n - i)])
		for j in range(n - i):
			rr[i][j] = (rr[i - 1][j] - rr[i - 1][j + 1]) / (x[j] - x[j + i])
		print(
			f'Розділені різниці {i}-го порядку:\n'
			f'\t{list(map(lambda _: round(_, _round), rr[i]))}\n'
		)

	s = f'{round(rr[n - 1][0], _round)}'

	for k in range(1,n-1)[::-1]:
		s = f'(x - {round(x[k], _round)}) * ({s}) + {round(rr[k][0], _round)}'

	s = f'(x - {round(x[0], _round)}) * ({s}) + {round(y[0], _round)}'
	
	print(f'Інтерполюючий багаточлен:\n\tP_{n-1}(x) = {s}\n')

	return s


if __name__ == '__main__':
	a, b, n, h = -5, 7, 13, 1

	def f(x: float) -> float:
		return 1 / 2 * (abs(x - 4) + abs(x + 4))

	y = [f(a + i * h) for i in range(n)]

	s = interpolate_newton_equidistant(y, a, b, n, h)

	k = 1000
	xi = [a + i * (b - a) / k for i in range(k + 2)]
	yi = []
	fi = []
	omegai = []
	for x in xi:
		yi.append(eval(s))
		fi.append(f(x))
		omegai.append(fi[-1] - yi[-1])


	xt = [a + i * h for i in range(n)]
	yt = []
	for x in xt:
		yt.append(f(x))

	plt.figure(figsize=(20,20))
	plt.grid(True)
	plt.plot(xi, yi, 'b-', label=f'$P_{{{n-1}}}(x)$')
	plt.plot(xi, fi, 'r--', label=f'$f(x)$')
	plt.plot(xi, omegai, 'g-.', label=f'$\omega_{{{n-1}}}(x)$')
	plt.legend(loc='upper center', fontsize=20)
	plt.scatter(xt, yt, c='r', alpha=1)
	plt.show()
