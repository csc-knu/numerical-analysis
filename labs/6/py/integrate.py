#!/usr/bin/env python
import numpy as np
from typing import Callable


def rectangle(a: float, b: float, f: Callable[[np.array], np.array], 
        h: float) -> float:
    return h * np.sum(f(np.arange(a + h / 2, b + h / 2, h)))


def trapezoid(a: float, b: float, f: Callable[[np.array], np.array], 
        h: float) -> float:
    return h / 2 * (f(a) + 2 * np.sum(f(np.arange(a + h, b, h))) + f(b))


def simpson(a: float, b: float, f: Callable[[np.array], np.array], 
        h: float) -> float:
    return h / 6 * (f(a) + 2 * np.sum(f(np.arange(a + h, b, h))) + 
        4 * np.sum(f(np.arange(a + h / 2, b + h / 2, h))) + f(b))
