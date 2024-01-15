#!/usr/bin/env python3
"""Module the make a tuple out of a string and a float"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Function that returns a tuple"""

    return (k, v * v)
