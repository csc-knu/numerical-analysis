from math import atan, sin, cos
import numpy as np
from numpy.linalg import norm, eig

n, k_eps = 5, 1e-7


def a(i, j):
	if i != j:
		return (i + j - 1) / (2 * n)
	else:
		return n + 10 + (i + j - 1) / (2 * n)


A = np.matrix([[a(i, j) for j in range(1, n + 1)] for i in range(1, n + 1)])

print(f'Знайдені бібліотечною функцією власні значення:\n\t{eig(A)[0]}\n')


def t(A):
	return sum(sum(A[i,j]**2 if i != j else 0 for j in range(n)) for i in range(n))


def ml(A):
	M = max(max(abs(A[i,j]) if i != j else 0 for j in range(n)) for i in range(n))

	for m in range(n):
		for l in range(n):
			if m != l and abs(A[m, l]) == M:
				return m, l


it = 0
while t(A) >= k_eps:
	it += 1

	U = np.eye(n)

	i, j = ml(A)
	
	phi = atan(2 * A[i, j] / (A[i,i] - A[j,j])) / 2
	
	U[i, j], U[j, i], U[i, i], U[j, j] = - sin(phi), sin(phi), cos(phi), cos(phi)
	
	A = U.T * A * U

	print(f'На ітерації {it} маємо t(A) = {t(A)}.\n')

print(f'Знайдені нами власні значення:\n\t{[A[i, i] for i in range(n)]}\n')
