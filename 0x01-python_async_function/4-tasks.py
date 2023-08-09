#!/usr/bin/env python3
"""
This module contains an asynchronous coroutine.
"""

from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    This task calls task_wait_random a couple of times, 
    a function that returns an asyncio Task that spawns wait_random
    and then returns a list of delays
    """

    delay_list = []
    index = 0

    while index < n:
        delay = await task_wait_random(max_delay)
        delay_list.append(delay)
        index += 1

    return sorted(delay_list)
