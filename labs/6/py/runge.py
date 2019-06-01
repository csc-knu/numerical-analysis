#!/usr/bin/env python
import numpy as np
from typing import Callable
import integrate


def rectangle(a: float, b: float, f: Callable[[np.array], np.array], 
        h: float) -> float:
    I_h, I_half_h = integrate.rectangle(a, b, f, h), \
        integrate.rectangle(a, b, f, h / 2)
    return abs(I_half_h - I_h) / 3


def trapezoid(a: float, b: float, f: Callable[[np.array], np.array], 
        h: float) -> float:
    I_h, I_half_h = integrate.trapezoid(a, b, f, h), \
        integrate.trapezoid(a, b, f, h / 2)
    return abs(I_half_h - I_h) / 3


def simpson(a: float, b: float, f: Callable[[np.array], np.array], 
        h: float) -> float:
    I_h, I_half_h = integrate.simpson(a, b, f, h), \
        integrate.simpson(a, b, f, h / 2)
    return abs(I_half_h - I_h) / 15
