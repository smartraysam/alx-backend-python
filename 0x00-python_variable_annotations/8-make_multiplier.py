#!/usr/bin/env python3
"""Module that make multipliers"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Function that returns function that multiplies a float by multiplier"""

    def multiply_by_multiplier(number: float) -> float:
        """Function that multiplies a float by multiplier"""

        return number * multiplier

    return multiply_by_multiplier
