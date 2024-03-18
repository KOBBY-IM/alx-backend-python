#!/usr/bin/env python3
"""Tasks"""

from ast import List
import asyncio
from asyncio import Task
from 3-tasks import task_wait_random

task_wait_name = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    delays = []
    for _ in range(n):
        delay = await task_wait_random(max_delay)
        delays.append(delay)
    return delays