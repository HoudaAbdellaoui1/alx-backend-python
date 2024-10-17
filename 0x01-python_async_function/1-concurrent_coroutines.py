#!/usr/bin/env python3
"""
Asynchronous Random Delay Module.

This module provides `wait_n`, that spawn wait_random n times
 with the specified max_delay.

"""

from asyncio import sleep
from typing import List


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): The maximum delay for each wait_random call.

    Returns:
        List[float]: A list of the delays in ascending order.
    """
    delays: List[float] = []
    wait_random = __import__('0-basic_async_syntax').wait_random

    for _ in range(n):
        delay = await wait_random(max_delay)
        inserted = False

        for i in range(len(delays)):
            if delay < delays[i]:
                delays.insert(i, delay)
                inserted = True
                break
        if not inserted:
            delays.append(delay)

    return delays
