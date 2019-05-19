#include <algorithm>
#include <iostream>
#include <cmath>

#include "RootSeparation.h"

namespace NumericalAnalysis {
	// locates roots with given precision
	std::vector<segment> separateRoots(ldouble(*f)(ldouble), ldouble left, ldouble right, ldouble precision) {
		precision /= 2; // for safety reasons

		uint numNodes = ceill((right - left) / precision) + 1;
		ldouble step = (right - left) / (numNodes - 1);

		std::vector<ldouble> nodesGrid(numNodes);
		for (size_t i = 0; i < numNodes; ++i)
			nodesGrid[i] = left + i * step;

		std::vector<ldouble> nodesValues(numNodes);
		std::transform(std::begin(nodesGrid), std::end(nodesGrid), std::begin(nodesValues), f);

		std::vector<segment> answer;
		for (size_t i = 0; i + 1 < numNodes; ++i) 
			if (nodesValues[i] * nodesValues[i + 1] < 0 || nodesValues[i] == 0) 
				answer.push_back({ nodesGrid[i], nodesGrid[i + 1] });

		return answer;
	}
}
