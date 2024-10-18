#!/usr/bin/env python3
"""

This module provides the `measure_runtime` coroutine,
which measures the time taken to run `async_comprehension`
four times concurrently using `asyncio.gather`.
"""


import asyncio
import time
from typing import List


async def measure_runtime() -> float:
    """
    Measures the total runtime for executing `async_comprehension`
    four times concurrently.

    Returns:
        float: The total elapsed time in seconds
        for running the four coroutines.

    """
    generator = __import__('1-async_comprehension').async_comprehension

    s = time.perf_counter()
    await asyncio.gather(generator(), generator(), generator(), generator())
    elapsed = time.perf_counter() - s

    return elapsed
