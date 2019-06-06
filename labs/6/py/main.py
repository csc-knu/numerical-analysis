#!/usr/bin/env python
import numpy as np
from typing import Callable
import apriori_error
import integrate
import runge
import richardson
import adaptive


def rectangle(a: float, b: float, f: Callable[[np.array], np.array], h: float, 
        I_True: float, M_2: float) -> None:
	while runge.rectangle(a, b, f, h) > eps:
		h /= 2

	h /= 2

	I_h, I_half_h, I_richardson = integrate.rectangle(a, b, f, h), \
		integrate.rectangle(a, b, f, h / 2), richardson.rectangle(a, b, f, h)

	I_adaptive = adaptive.rectangle(a, b, f, eps)

	print(
		f'\nRECTANGLE:\n'
		f'\th                 = {h}\n'
		f'\tI_true            = {I_true}\n'
		f'\tI_h               = {I_h}\n'
		f'\tR_h_true          = {abs(I_true - I_h)}\n'
		f'\tI_half_h          = {I_half_h}\n'
		f'\tR_half_h_true     = {abs(I_true - I_half_h)}\n'
		f'\tR_runge           = {runge.rectangle(a, b, f, h)}\n'
		f'\tI_richardson      = {I_richardson}\n'
		f'\tR_richardson_true = {abs(I_true - I_richardson)}\n'
		f'\tapriori_error     = {apriori_error.rectangle(a, b, M_2, h)}\n'
		f'\tI_apadtive        = {I_adaptive}\n'
		f'\tR_apadtive        = {abs(I_true - I_adaptive)}\n'
	)


def trapezoid(a: float, b: float, f: Callable[[np.array], np.array], h: float, 
        I_True: float, M_2: float) -> None:
	while runge.trapezoid(a, b, f, h) > eps:
		h /= 2

	h /= 2

	I_h, I_half_h, I_richardson = integrate.trapezoid(a, b, f, h), \
		integrate.trapezoid(a, b, f, h / 2), richardson.trapezoid(a, b, f, h)

	I_adaptive = adaptive.trapezoid(a, b, f, eps)

	print(
		f'TRAPEZOID:\n'
		f'\th                 = {h}\n'
		f'\tI_true            = {I_true}\n'
		f'\tI_h               = {I_h}\n'
		f'\tR_h_true          = {abs(I_true - I_h)}\n'
		f'\tI_half_h          = {I_half_h}\n'
		f'\tR_half_h_true     = {abs(I_true - I_half_h)}\n'
		f'\tR_runge           = {runge.trapezoid(a, b, f, h)}\n'
		f'\tI_richardson      = {I_richardson}\n'
		f'\tR_richardson_true = {abs(I_true - I_richardson)}\n'
		f'\tapriori_error     = {apriori_error.trapezoid(a, b, M_2, h)}\n'
		f'\tI_apadtive        = {I_adaptive}\n'
		f'\tR_apadtive        = {abs(I_true - I_adaptive)}\n'
	)


def simpson(a: float, b: float, f: Callable[[np.array], np.array], h: float, 
        I_True: float, M_4: float) -> None:
	while runge.simpson(a, b, f, h) > eps:
		h /= 2

	h /= 2

	I_h, I_half_h, I_richardson = integrate.simpson(a, b, f, h), \
		integrate.simpson(a, b, f, h / 2), richardson.simpson(a, b, f, h)

	I_adaptive = adaptive.simpson(a, b, f, eps)

	print(
		f'SIMPSON:\n'
		f'\th                 = {h}\n'
		f'\tI_true            = {I_true}\n'
		f'\tI_h               = {I_h}\n'
		f'\tR_h_true          = {abs(I_true - I_h)}\n'
		f'\tI_half_h          = {I_half_h}\n'
		f'\tR_half_h_true     = {abs(I_true - I_half_h)}\n'
		f'\tR_runge           = {runge.simpson(a, b, f, h)}\n'
		f'\tI_richardson      = {I_richardson}\n'
		f'\tR_richardson_true = {abs(I_true - I_richardson)}\n'
		f'\tapriori_error     = {apriori_error.simpson(a, b, M_4, h)}\n'
		f'\tI_apadtive        = {I_adaptive}\n'
		f'\tR_apadtive        = {abs(I_true - I_adaptive)}\n'
	)


if __name__ == '__main__':
	def f(t):
		return 3 * t * np.log(2 + t)

	a, b = -1, 1
	I_true = 6 - 9 / 2 * np.log(3)

	M_2, M_4 = 9, 42

	h = b - a
	eps = 1e-5
	
	rectangle(a, b, f, h, I_true, M_2)
	trapezoid(a, b, f, h, I_true, M_2)
	simpson(a, b, f, h, I_true, M_4)
