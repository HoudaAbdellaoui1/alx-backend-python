#!/usr/bin/env python3
"""
Measure runtime Module.

This module provides `measure_time`, that measures the total
execution time for wait_n

"""

import asyncio
import time


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): The maximum delay for each wait_random call.

    Returns:
        float: total execution time.
    """
    wait_n = __import__('1-concurrent_coroutines').wait_n
    s = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed = time.perf_counter() - s

    return elapsed / n
