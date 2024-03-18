#!/usr/bin/env python3
"""Tasks"""

import asyncio
from asyncio import Task
from random import randint


async def wait_random(max_delay: int) -> float:
    """Asynchronous routine that waits for a random delay between 0
    and max_delay (included)and returns it.
    """
    delay = randint(0, max_delay)
    await asyncio.sleep(delay)
    return delay
