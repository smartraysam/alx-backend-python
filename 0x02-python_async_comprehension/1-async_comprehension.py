#!/usr/bin/env python3
"""Module that returns random numbers generated asynchronously"""
from typing import List


async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """Return list of random numbers generated asynchronously"""
    return [i async for i in async_generator()]
