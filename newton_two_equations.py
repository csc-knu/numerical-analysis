from math import sin, cos, sqrt
from typing import Callable, Tuple
import unittest


def newton_two_equations(f: Callable[[float, float], float], 
	f_prime_x: Callable[[float, float], float], f_prime_y: Callable[[float, float], float], 
	g: Callable[[float, float], float], g_prime_x: Callable[[float, float], float], 
	g_prime_y: Callable[[float, float], float], x0: float, y0: float, eps: float=1e-7, 
	kmax: int=1e3) -> Tuple[float, float]:
	"""
	solves f(x, y) = g(x, y) = 0 by Newton's method with precision eps
	:param f: f
	:param f_prime_x: f'_x
	:param f_prime_y: f'_y
	:param g: g
	:param g_prime_x: g'_x
	:param g_prime_y: g'_y
	:param x0: starting x
	:param y0: starting y
	:param eps: precision wanted
	:return: root (x, y)
	"""
	x, x_prev, y, y_prev, i = x0, x0 + 2 * eps, y0, y0 + 2 * eps, 1
	
	while sqrt((x - x_prev)**2 + (y - y_prev)**2) >= eps and i <= kmax:
		dk = f_prime_x(x, y) * g_prime_y(x, y) - f_prime_y(x, y) * g_prime_x(x, y)
		dkx = f(x, y) * g_prime_y(x, y) - f_prime_y(x, y) * g(x, y)
		dky = f_prime_x(x, y) * g(x, y) - f(x, y) * g_prime_x(x, y)
		x, x_prev, y, y_prev, i = x - dkx / dk, x, y - dky / dk, y, i + 1

	return x, y


class TestNewton(unittest.TestCase):
	def test_0(self):
		def f(x: float, y: float) -> float:
			return sin(x - .5 * y) - x + y**2


		def f_prime_x(x: float, y: float) -> float:
			return cos(x - .5 * y) - 1


		def f_prime_y(x: float, y: float) -> float:
			return 2 * y - .5 * cos(x - .5 * y)


		def g(x: float, y: float) -> float:
			return (y + .1)**2 + x**2 - .6


		def g_prime_x(x: float, y: float) -> float:
			return 2 * x


		def g_prime_y(x: float, y: float) -> float:
			return 2 * (y + .1)


		x0, y0, x_star, y_star = .1, .1, 0.4847661895550592, 0.5041537399240928

		x, y = newton_two_equations(f, f_prime_x, f_prime_y, g, g_prime_x, g_prime_y, x0, y0)

		err = sqrt((x - x_star)**2 + (y - y_star)**2)

		self.assertAlmostEqual(err, 0)


if __name__ == '__main__':
	unittest.main()
