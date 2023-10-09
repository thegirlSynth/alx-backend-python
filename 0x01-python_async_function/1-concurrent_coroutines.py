#!/usr/bin/env python3
"""
This module contains an asynchronous coroutine.
"""

from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    This coroutine spawns wait_random a couple of times,
    and then returns a list of delays
    """

    delay_list = []
    index = 0

    for i in range(n):
        delay = await wait_random(max_delay)
        delay_list.append(delay)
        index += 1

    return sorted(delay_list)
