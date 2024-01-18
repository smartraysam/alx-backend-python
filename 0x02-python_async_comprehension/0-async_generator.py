#!/usr/bin/env python3
"""module that returns a random number between 0 and 10 asynchronously"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """coroutine that yields a random number between 0 and 10"""

    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
