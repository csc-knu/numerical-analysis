#pragma once

#include <vector>

typedef long double ldouble;
typedef unsigned int uint;

namespace NumericalAnalysis {
	ldouble findRootNewton(ldouble(*f)(ldouble), ldouble(*f_prime)(ldouble), ldouble left, ldouble right, ldouble x0, ldouble precision, uint p);
	ldouble findRootSecant(ldouble(*f)(ldouble), ldouble left, ldouble right, ldouble x0, ldouble x1, ldouble precision, uint p);
	ldouble findRootChord(ldouble(*f)(ldouble), ldouble left, ldouble right, ldouble x0, ldouble precision, uint p);
	ldouble findRootSimpleIterate(ldouble(*f)(ldouble), ldouble left, ldouble right, ldouble x0, ldouble precision, ldouble m1, ldouble M1);
}
