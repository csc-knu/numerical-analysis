import numpy as np

ITERATION_LIMIT = 1000

# initialize the matrix
A = np.array([[10., -1., 2., 0.],
              [-1., 11., -1., 3.],
              [2., -1., 10., -1.],
              [0., 3., -1., 8.]])

# initialize the RHS vector
b = np.array([6., 25., -11., 15.])

print("System of equations:")

for i in range(A.shape[0]):
    row = [f"{A[i, j]:3g}*x{j + 1}" for j in range(A.shape[1])]

    print(f'[{" + ".join(row)}] = [{b[i]:3g}]')

x = np.zeros_like(b)

for it_count in range(1, ITERATION_LIMIT):

    x_new = np.zeros_like(x)

    print(f"Iteration {it_count}: {x}")

    for i in range(A.shape[0]):
        s1 = np.dot(A[i, :i], x_new[:i])

        s2 = np.dot(A[i, i + 1:], x[i + 1:])

        x_new[i] = (b[i] - s1 - s2) / A[i, i]

    if np.allclose(x, x_new, rtol=1e-8):
        break

    x = x_new

print(f"Solution: {x}")

error = np.dot(A, x) - b

print(f"Error: {error}")
