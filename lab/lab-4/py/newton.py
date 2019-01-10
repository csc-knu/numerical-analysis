#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""chebyshev.py: interpolates function f(x) 
by a give grid y of values for x in [a, b] 
via Newton method with equidistant nodes."""
import matplotlib.pyplot as plt


def interpolate_newton_equidistant(y, a, b, n, h, log=False):
	x = [a + i * h for i in range(n)]

	if log:
		print(f'\nВузли інтерполяції:\n'
			f'\t{[round(xi, _round) for xi in x]}\n\n')

	if log:
		print(f'Значення функції у вузлах:\n'
			f'\t{[round(_, _round) for _ in y]}\n\n')

	rr = [x, [(y[i] - y[i + 1]) / (x[i] - x[i + 1]) for i in range(n - 1)]]

	if log:
		print(f'Розділені різниці 1-го порядку:\n'
			f'\t{[round(_, _round) for _ in rr[1]]}\n\n')

	for i in range(2, n):
		rr.append([0 for _ in range(n - i)])

		for j in range(n - i):
			rr[i][j] = (rr[i - 1][j] - rr[i - 1][j + 1]) / (x[j] - x[j + i])

		if log:
			print(f'Розділені різниці {i}-го порядку:\n'
				f'\t{[round(_, _round) for _ in rr[i]]}\n\n')

	pn = f'{round(rr[n - 1][0], _round)}'

	for k in range(1,n-1)[::-1]:
		pn = f'(x - {round(x[k], _round)}) * ({pn}) + {round(rr[k][0], _round)}'

	pn = f'(x - {round(x[0], _round)}) * ({pn}) + {round(y[0], _round)}'

	if log:
		print(f'Інтерполюючий багаточлен:\n'
			f'\tP_{n-1}(x) = {pn}\n')

	return pn


if __name__ == '__main__':
	plt.rcParams.update({'font.size': 22})

	def f(x: float) -> float:
		return 1 / 2 * (abs(x - 4) + abs(x + 4))

	a, b, n, h, _round, k = -5, 7, 13, 1, 9, 1000

	y = [f(a + i * h) for i in range(n)]

	pn = interpolate_newton_equidistant(y, a, b, n, h, log=True)

	_x = [a + i * (b - a) / k for i in range(k + 1)]

	y, _f = [eval(pn) for x in _x], [f(x) for x in _x]
	omega =[y[i] - _f[i] for i in range(k + 1)]

	plt.figure(figsize=(20,20))

	plt.grid(True)

	plt.plot(_x, y, 'b-', label=f'$P_{{{n-1}}}(x)$')
	plt.plot(_x, _f, 'r--', label=f'$f(x)$')
	plt.plot(_x, omega, 'g-.', label=f'$\omega_{{{n-1}}}(x)$')

	_x = [a + i * h for i in range(n)]
	y = [f(x) for x in _x]

	plt.scatter(_x, y, c='r', alpha=1)

	plt.legend(loc='upper center', fontsize=22)

	plt.show()


__author__: "Nikita Skybytskyi"
__copyright__ = "Copyright 2019, KNU"
__credits__ = ["Nikita Skybytskyi"]
__license__ = "MIT"
__version__ = "1.1.2"
__maintainer__ = "Nikita Skybytskyi"
__email__ = "n.skybytskyi@knu.ua"
__status__ = "Production"
