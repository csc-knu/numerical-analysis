import numpy as np
from numpy.linalg import norm, eig

n = 5


def a(i, j):
	if i != j:
		return (i + j - 1) / (2 * n)
	else:
		return n + 10 + (i + j - 1) / (2 * n)


A = np.matrix([[a(i, j) for j in range(1, n + 1)] for i in range(1, n + 1)])

# print(f'A = {A}')

print(f'eig(A) = {eig(A)}')

x = [np.matrix([1, 0, 0, 0, 0]).T]

mu1 = []

for iteration in range(0):
	print(f'iteration = {iteration}')

	print(f'xi = {x[-1]}')

	x.append(A * (x[-1]))

	mu1.append(float(x[-1].T * x[-2]) / float(x[-2].T * x[-2]))

	x[-1] /= norm(x[-1], 2)

	print(f'mu1i = {mu1[-1]}')

B = 17.686140661634397 * np.eye(n) - A

x = [np.matrix([1, 0, 0, 0, 0]).T]

mu1 = []

for iteration in range(0):
	print(f'iteration = {iteration}')

	print(f'xi = {x[-1]}')

	x.append(B * (x[-1]))

	mu1.append(float(x[-1].T * x[-2]) / float(x[-2].T * x[-2]))

	x[-1] /= norm(x[-1], 2)

	print(f'mu1i = {mu1[-1]}')

C = np.eye(n) - (A * A) / 17.686140661634397**2

print(f'C = {C}')

x = [np.matrix([1, 0, 0, 0, 0]).T]

mu1 = []

for iteration in range(100):
	print(f'iteration = {iteration}')

	print(f'xi = {x[-1]}')

	x.append(C * (x[-1]))

	mu1.append(float(x[-1].T * x[-2]) / float(x[-2].T * x[-2]))

	x[-1] /= norm(x[-1], 2)

	print(f'mu1i = {mu1[-1]}')
