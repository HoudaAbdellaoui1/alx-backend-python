#!/usr/bin/env python3
"""
Task Creation Module.

This module provides a function `task_wait_random` that creates
and returns an asyncio.Task that runs the `wait_random` coroutine.

"""

from asyncio import Task, create_task
from typing import List


def task_wait_random(max_delay: int) -> Task:
    """
    Create and return an asyncio.Task for the wait_random coroutine.

    Args:
        max_delay (int): The maximum delay for wait_random.

    Returns:
        asyncio.Task: A task object that runs the wait_random coroutine.
    """
    wait_random = __import__('0-basic_async_syntax').wait_random
    return create_task(wait_random(max_delay))
