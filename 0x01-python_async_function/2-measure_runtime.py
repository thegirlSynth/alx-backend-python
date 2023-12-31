#!/usr/bin/env python3
"""
This module contains an asynchronous coroutine.
"""

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    This coroutine measures the total execution time for wait_n(n, max_delay),
    and returns total_time / n
    """

    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()

    total_time = end_time - start_time
    avg_time = total_time/n

    return avg_time
