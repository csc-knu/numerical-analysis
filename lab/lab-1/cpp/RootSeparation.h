#pragma once

#include <vector>

typedef long double ldouble;
typedef unsigned int uint;

namespace NumericalAnalysis {
	struct segment { ldouble left, right; }; 
	std::vector<segment> separateRoots(ldouble(*f)(ldouble), ldouble left, ldouble right, ldouble precision);
}