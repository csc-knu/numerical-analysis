#include <iostream>
#include <iterator>
#include <cassert>

#include "RootSeparation.h"

namespace NumericalAnalysis {
	void testcase_1() {
		ldouble left = -10, right = 10, precision = .1;

		auto f = [](ldouble x) { return (x - 2) * (x - 3) * (x + 5); };

		auto res = separateRoots(f, left, right, precision);

		assert((std::size(res) == 3 && "wrong number of segments returned"));

		assert(fabsl(res[0].left + 5) <= precision && "left endpoint of first segment returned is too far from -5");
		assert(fabsl(res[0].right + 5) <= precision && "right endpoint of first segment returned is too far from -5");

		assert(fabsl(res[1].left - 2) <= precision && "left endpoint of second segment returned is too far from 2");
		assert(fabsl(res[1].right - 2) <= precision && "right endpoint of second segment returned is too far from 2");
		
		assert(fabsl(res[2].left - 3) <= precision && "left endpoint of third segment returned is too far from 3");
		assert(fabsl(res[2].right - 3) <= precision && "right endpoint of third segment returned is too far from 3");
	}
}