#!/usr/bin/env python3
"""
Run time for four parallel comprehensions
"""

import asyncio
import time

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
    Collects 10 random numbers using an async comprehensing over
    async_generator, then returns the 10 random numbers.
    """
    time_start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    total_time = time.perf_counter() - time_start

    return total_time
