#include <algorithm>
#include <cmath>

#include "RootFinding.h"

namespace NumericalAnalysis {
	// p is the degree of a root
	ldouble findRootNewton(ldouble(*f)(ldouble), ldouble(*f_prime)(ldouble),
		ldouble left, ldouble right, ldouble x0, ldouble precision, uint p = 1) {
		ldouble x_now = x0 - p * f(x0) / f_prime(x0), x_prev = x0;

		while (fabsl(x_now - x_prev) >= precision) {
			x_prev = x_now;
			x_now = x_prev - p * f(x_prev) / f_prime(x_prev);
		}

		return x_now;
	}

	// Newton with numerical differentiation
	ldouble findRootSecant(ldouble(*f)(ldouble), ldouble left, ldouble right,
		ldouble x0, ldouble x1, ldouble precision, uint p = 1) {
		ldouble x_next = x1 - p * f(x1) / (f(x1) - f(x0)) * (x1 - x0),
			x_now = x1, x_prev = x0;

		while (fabsl(x_next - x_now) >= precision) {
			x_prev = x_now;
			x_now = x_next;
			x_next = x_now - p * f(x_now) / (f(x_now) - x_prev) * (x_now - x_prev);
		}

		return x_next;
	}

	// for f'' > 0 only
	ldouble findRootChord(ldouble(*f)(ldouble), ldouble left, ldouble right,
		ldouble x0, ldouble precision, uint p = 1) {
		if (f(left) < 0) {
			ldouble x_now = x0 - f(x0) / (f(right) - f(x0)) * (right - x0), x_prev = x0;

			while (fabsl(x_now - x_prev) >= precision) {
				x_prev = x_now;
				x_now = x_prev - f(x_prev) * (f(right) - f(x_prev)) * (right - x_prev);
			}

			return x_now;
		}
		else {
			ldouble x_now = x0 - f(x0) / (f(x0) - f(left)) * (x0 - left), x_prev = x0;

			while (fabsl(x_now - x_prev) >= precision) {
				x_prev = x_now;
				x_now = x_prev - f(x_prev) * (f(x_prev) - f(left)) * (x_prev - left);
			}

			return x_now;
		}
	}

	// for 0 < m1 < f' < M1 only
	ldouble findRootSimpleIterate(ldouble(*f)(ldouble), ldouble left, ldouble right,
		ldouble x0, ldouble precision, ldouble m1, ldouble M1) {
		auto phi = [f, M1](ldouble x) -> ldouble { return x - f(x) / M1; };

		ldouble q = 1 - m1 / M1;

		ldouble x_now = phi(x0), x_prev = x0;

		while (fabsl(x_now - x_prev) >= (1 - q) / q * precision) {
			x_prev = x_now;
			x_now = phi(x_prev);
		}

		return x_now;
	}
}
