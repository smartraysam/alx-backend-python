#!/usr/bin/env python3
"""Module that get element length"""
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Function that returns the sum of a list of floats"""

    return [(i, len(i)) for i in lst]
