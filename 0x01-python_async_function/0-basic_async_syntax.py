#!/usr/bin/env python3
"""Basic asynchronous syntax"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Asynchronous coroutine that takes in an integer argument
    (max_delay, with a default value of 10) named max_delay and returns a
    random float value with the specified max_delay
    """

    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
