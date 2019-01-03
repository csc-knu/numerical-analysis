#!/usr/bin/env python
from math import sin


def simple_iterate(f, a, b, M1, x0, eps=1e-7, kmax=1e3):
	x, x_prev, i = x0, x0 + 2 * eps, 1
	
	def phi(x: float) -> float:
		return x - (1 / M1) * f(x)

	while (abs(x - x_prev) >= eps or f(x) >= eps) and i <= kmax:
		print(f'На ітерації {i} маємо:\n\tx = {x},\n\tr = {abs(x_star - x)}.\n')
		x, x_prev, i = phi(x), x, i + 1

	return x


def f(x: float) -> float:
	return x**2 - 20 * sin(x)


a, b, M1, x0, x_star = 2, 3, 25.7998499320089, 2, 2.7529466338187049383

print(f'"Справжній" розв\'язок x_star = {x_star}\n')

x = simple_iterate(f, a, b, M1, x0)

print(f"Знайдений нами розв'язок x = {x}\n")

print(f"Похибка: {abs(x - x_star)}")
