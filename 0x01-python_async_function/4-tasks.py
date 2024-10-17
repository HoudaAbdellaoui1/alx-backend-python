#!/usr/bin/env python3
"""
Asynchronous Random Delay Module.

This module provides `task_wait_n`, that spawn task_wait_random n times
 with the specified max_delay.

"""

from asyncio import sleep
from typing import List


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times with the specified max_delay.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): The maximum delay for each wait_random call.

    Returns:
        List[float]: A list of the delays in ascending order.
    """
    delays: List[float] = []
    task_wait_random = __import__('3-tasks').task_wait_random

    for _ in range(n):
        delay = await task_wait_random(max_delay)
        inserted = False

        for i in range(len(delays)):
            if delay < delays[i]:
                delays.insert(i, delay)
                inserted = True
                break
        if not inserted:
            delays.append(delay)

    return delays
