#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""scalar_products.py: finds several eigenvalues of a given matrix A."""
import numpy as np
from numpy.linalg import norm, eig


def _a(i, j):
	"""
	:param i: row of entry of a to generate
	:param j: row of entry of a to generate
	"""
	if i != j:
		return (i + j - 1) / (2 * n)
	else:
		return n + 10 + (i + j - 1) / (2 * n)


def eig_max_abs(a, eps=1e-7, kmax=1e3, log=False):
	""" 
	:param a: matrix to find max by absolute value eigenvalue of
	:param eps: desired precision
	:param kmax: max number of iterations allowed
	:param log: whether to log the iterations
	"""
	x_prev = np.zeros(a.shape[0])[np.newaxis].T
	
	x_prev[0] = 1.

	x = a * x_prev

	mu = float(np.dot(x.T, x_prev) / np.dot(x_prev.T, x_prev))

	mu_prev = mu + 2 * eps

	x /= norm(x, 2)

	def _next():
		nonlocal mu_prev, mu, x_prev, x, i
		i += 1

		x, x_prev = a * x, x
		
		mu, mu_prev = float(np.dot(x.T, x_prev) / np.dot(x_prev.T, x_prev)), mu
		
		x /= norm(x, 2)

	def _log():
		print(f'\nНа ітерації {i} маємо \n'
			f'\t x_i = {x.T}\n'
			f'\tmu_i = {mu}\n')

	i = 0

	while abs(mu - mu_prev) > eps and i <= kmax:
		_next()
		if log:
			_log()

	return mu


def eig_min(a, eps=1e-7, kmax=1e3, log=False):

	""" 
	:param a: matrix to find min eigenvalue of
	:param eps: desired precision
	:param kmax: max number of iterations allowed
	:param log: whether to log the iterations
	"""
	mu_1 = eig_max_abs(a, eps, kmax, log)

	return mu_1 - eig_max_abs(mu_1 * np.eye(a.shape[0]) - a, eps, kmax, log)


def eig_min_abs(a, eps=1e-7, kmax=1e3, log=False):

	""" 
	:param a: matrix to find min by absolute value eigenvalue of
	:param eps: desired precision
	:param kmax: max number of iterations allowed
	:param log: whether to log the iterations
	"""
	mu_1 = eig_max_abs(a, eps, kmax, log)

	mu_2 = eig_max_abs(np.eye(a.shape[0]) - (a * a) / mu_1**2, eps, kmax, log)

	return np.sqrt(mu_1**2 * (1 - mu_2))


if __name__ == '__main__':
	np.set_printoptions(linewidth=90)

	n = 6

	a = np.matrix([[_a(i, j) for j in range(1, n)] for i in range(1, n)])

	# part 1

	lib_mu = np.max(np.abs(eig(a)[0]))

	mu = eig_max_abs(a)

	print(f'\nЗнайдене бібліотечною функцією найбільше (за модулем) '
		f'власне значення:\n'
		f'\tλ = {lib_mu}\n\n')

	print(f'Знайдене нами найбільше за модулем власне значення:\n'
		f'\tλ = {mu}\n\n')

	print(f'Похибка обчислень:\n'
		f'\tr = {abs(lib_mu - mu)}\n\n')

	# part 2

	lib_mu = np.min(eig(a)[0])

	mu = eig_min(a)

	print(f'Знайдене бібліотечною функцією найменше власне значення:\n'
		f'\tλ = {lib_mu}\n\n')

	print(f'Знайдене нами найменше власне значення:\n'
		f'\tλ = {mu}\n\n')

	print(f'Похибка обчислень:\n'
		f'\tr = {abs(lib_mu - mu)}\n\n')

	# part 3

	lib_mu = np.min(abs(eig(a)[0]))

	mu = eig_min_abs(a)

	print(f'Знайдене бібліотечною функцією найменше (за модулем) '
		f'власне значення:\n'
		f'\tλ = {lib_mu}\n\n')

	print(f'Знайдене нами найменше за модулем власне значення:\n'
		f'\tλ = {mu}\n\n')

	print(f'Похибка обчислень:\n'
		f'\tr = {abs(lib_mu - mu)}\n')


__author__: "Nikita Skybytskyi"
__copyright__ = "Copyright 2019, KNU"
__credits__ = ["Nikita Skybytskyi"]
__license__ = "MIT"
__version__ = "1.1"
__maintainer__ = "Nikita Skybytskyi"
__email__ = "n.skybytskyi@knu.ua"
__status__ = "Production"
