#!/usr/bin/env python3
"""Concurrent coroutines"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: float) -> List[float]:
    """
    Asynchronous coroutine that takes in two
    integer arguments (n and max_delay,)
    """
    delays = []
    for _ in range(n):
        delay = await wait_random(max_delay)
        delays.append(delay)
    return delays
