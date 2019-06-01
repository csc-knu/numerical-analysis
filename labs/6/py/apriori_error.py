#!/usr/bin/env python


def rectangle(a: float, b: float, M_2: float, h: float) -> float:
    return M_2 * h**2 * (b - a) / 24


def trapezoid(a: float, b: float, M_2: float, h: float) -> float:
    return M_2 * h**2 * (b - a) / 12


def simpson(a: float, b: float, M_4: float, h: float) -> float:
    return M_4 * h**4 * (b - a) / 2880
