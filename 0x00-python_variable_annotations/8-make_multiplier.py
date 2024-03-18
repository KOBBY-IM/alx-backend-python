#!/usr/bin/env python3
""" module containing a function make_multiplier """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
      Takes a float multiplier as argument and returns a
      function that multiplies a float by multiplier.
    """
    def multiply(num: float) -> float:
        return num * multiplier
    return multiply
