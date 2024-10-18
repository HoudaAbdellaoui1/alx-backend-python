#!/usr/bin/env python3
"""
Asynchronous Random Delay Module.

This module provides an `async_generator` function that asynchronously
yields random floating-point numbers after waiting for a short delay.
It demonstrates asynchronous generators in Python.
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Asynchronously yield random numbers between 1 and 10,
    waiting 1 second between each.

    This function uses an asynchronous generator to yield
    a random floating-point number
    after waiting for 1 second. It yields a total of 10 random numbers.

    Yields:
        float: Random floating-point number between 1 and 10.

    Example:
        >>> async for value in async_generator():
        >>>     print(value)
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(1, 10)
