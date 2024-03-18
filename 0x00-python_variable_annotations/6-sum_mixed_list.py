#!/usr/bin/env python3
"""Module containing a function sum_mixed_list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns sum of a list of integers and floats"""
    return float(sum(mxd_lst))