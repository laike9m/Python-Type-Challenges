"""
TODO:

`gen` is a generator that yields a integer, and can accept a string sent to it.
It does not return anything.
"""

from collections.abc import Generator


def gen() -> Generator[int, str, None]:
    """You don't need to implement it"""
    ...


## End of your code ##
from typing import assert_type

generator = gen()
assert_type(next(generator), int)
generator.send("sss")
generator.send(3)  # expect-type-error
