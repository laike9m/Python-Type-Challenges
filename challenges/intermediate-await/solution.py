"""
TODO:

`run_async` takes an awaitable integer.
"""

from typing import Awaitable


def run_async(func: Awaitable[int]):
    ...


## End of your code ##
from asyncio import Queue

queue: Queue[int] = Queue()
queue2: Queue[str] = Queue()


async def async_function() -> int:
    return await queue.get()


async def async_function2() -> str:
    return await queue2.get()


run_async(async_function())
run_async(1)  # expect-type-error
run_async(async_function2())  # expect-type-error
