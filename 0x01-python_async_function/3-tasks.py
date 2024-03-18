#!/usr/bin/env python3
"""Tasks"""

import asyncio
from typing import Any
from asyncio import Task

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """Take an integer max_delay and return a Task"""
    return asyncio.create_task(wait_random(max_delay))
