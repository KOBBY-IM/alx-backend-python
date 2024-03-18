#!/usr/bin/env python3
""" module containing a function element_length  """
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Annotates the parameters and return values of the element_length function.

    Parameters:
        lst (Iterable[Sequence]): A list-like iterable containing sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each
        tuple contains a sequence from lst and its length.
    """
    return [(i, len(i)) for i in lst]
