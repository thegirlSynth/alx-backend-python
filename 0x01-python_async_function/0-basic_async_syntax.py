#!/usr/bin/env python3
"""
This module contains an asynchronous coroutine.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    This coroutine waits for a random delay, and then returns it
    """

    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
