#!/usr/bin/env python
import numpy as np
from typing import Callable
import runge
import integrate


def rectangle(a: float, b: float, f: Callable[[np.array], np.array], 
        eps: float) -> float:
    if runge.rectangle(a, b, f, b - a) < eps:
        return integrate.rectangle(a, b, f, b - a)
    else:
        m = (a + b) / 2
        return rectangle(a, m, f, eps / 2) + rectangle(m, b, f, eps / 2)


def trapezoid(a: float, b: float, f: Callable[[np.array], np.array], 
        eps: float) -> float:
    if runge.trapezoid(a, b, f, b - a) < eps:
        return integrate.trapezoid(a, b, f, b - a)
    else:
        m = (a + b) / 2
        return trapezoid(a, m, f, eps / 2) + trapezoid(m, b, f, eps / 2)


def simpson(a: float, b: float, f: Callable[[np.array], np.array], 
        eps: float) -> float:
    if runge.simpson(a, b, f, b - a) < eps:
        return integrate.simpson(a, b, f, b - a)
    else:
        m = (a + b) / 2
        return simpson(a, m, f, eps / 2) + simpson(m, b, f, eps / 2)
