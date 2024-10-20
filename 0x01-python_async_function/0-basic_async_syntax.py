#!/usr/bin/env python3
"""
Asynchronous Random Delay Module.

This module provides `wait_random`, that waits for
a random delay between 0 and a specified maximum number of seconds.

"""

from asyncio import sleep
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronously wait for a random delay between 0
    and max_delay seconds.

    Args:
        max_delay (int, optional): The maximum value for the random delay.
                                   Default is 10 seconds.

    Returns:
        float: The actual random delay time
        that the coroutine waited for.
    """
    delay = random.random() * max_delay
    await sleep(delay)
    return delay
