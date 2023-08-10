#!/usr/bin/env python3
"""
Complex types - functions
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by multiplier.
    """

    def multiply_by_multiplier(num: float) -> float:
        """
        Multiplies a float by multiplier.
        """
        return num * multiplier

    return multiply_by_multiplier
