e[0] = x[0] / norm(x[0])

k = 0
while True:
	k += 1

	x[k + 1] = A * x[k]
	μ[k][1] = scalar_product(x[k + 1], e[k])
	e[k + 1] = x[k + 1] / norm(x[k + 1])

	if abs(μ[k + 1][1] - μ[k][1]) < ε:
		break

λ[1] = μ[k + 1][1]
