#!/usr/bin/env python3
'''This module provides an asynchronous generator function that yields a
random float between 0 and 10 after a one second delay for a total of
10 iterations.
'''
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    '''Generates a sequence of 10 numbers.
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
