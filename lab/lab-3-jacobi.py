#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""jacobi.py: finds all eigenvalues of a given symmetric matrix A."""
from math import atan, sin, cos
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


def t(a):
	"""
	:param a: matrix to find t-function of
	:return: t(a) = off-diagonal elements' sum of squares
	"""
	return np.sum(np.power(a - np.eye(a.shape[0]) * np.diag(a), 2))


def max_ij(a):
	"""
	:param a: matrix to find the leading element of
	:return: m, l = argmax |a_ij| over i, j
	"""
	_a = np.abs(a - np.eye(a.shape[0]) * np.diag(a))
	m = np.max(_a)

	_i, _j = np.where(_a == m)

	return _i[0], _j[0]


def jacobi(a, eps=1e-7):
	""" 
	:param a: matrix to find eigenvalues of
	:param eps: desired precision
	"""
	it = 0
	while t(a) >= eps:
		it += 1

		u = np.eye(a.shape[0])

		i, j = max_ij(a)
		
		phi = atan(2 * a[i, j] / (a[i,i] - a[j,j])) / 2
		
		u[i, [i, j]],u[j, [i, j]] = [cos(phi), - sin(phi)], [sin(phi), cos(phi)]
		
		a = u.T * a * u

		print(f'\nНа ітерації {it} маємо \n'
			f'\tt(a) = {t(a)}.\n')

	return np.sort(np.diag(a))


if __name__ == '__main__':
	np.set_printoptions(linewidth=90)

	n = 6

	a = np.matrix([[_a(i, j) for j in range(1, n)] for i in range(1, n)])

	lib_eig = np.array(sorted(eig(a)[0]))

	jacobi_eig = jacobi(a)

	print(f'\nЗнайдені бібліотечною функцією власні значення:\n'
		f'\tλ = {lib_eig}\n\n')

	print(f'Знайдені нами власні значення:\n'
		f'\tλ = {jacobi_eig}\n\n')

	print(f'Вектор нев\'язки:\n'
		f'\tr = {lib_eig - jacobi_eig}\n')


__author__: "Nikita Skybytskyi"
__copyright__ = "Copyright 2019, KNU"
__credits__ = ["Nikita Skybytskyi"]
__license__ = "MIT"
__version__ = "1.1.1"
__maintainer__ = "Nikita Skybytskyi"
__email__ = "n.skybytskyi@knu.ua"
__status__ = "Production"
