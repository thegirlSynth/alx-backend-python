#!/usr/bin/env python3
"""
Contains a coroutine async_generator"
"""

import asyncio
import random


async def async_generator() -> Generator[float, None, None]:
    """
    Generates 10 random floats between 0 and 10
    """

    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
