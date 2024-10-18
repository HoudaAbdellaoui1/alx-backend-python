#!/usr/bin/env python3
"""
Asynchronous Comprehension Module.

This module provides the `async_comprehension` coroutine,
which collects random numbers asynchronously using
an async comprehension over `async_generator`.
"""


from typing import List


async def async_comprehension() -> List[float]:
    """
    Collect 10 random numbers using an async comprehension
    over async_generator.


    Returns:
        List[float]: A list of 10 random floating-point numbers.
    """
    generator = __import__('0-async_generator').async_generator

    return [number async for number in generator()]
