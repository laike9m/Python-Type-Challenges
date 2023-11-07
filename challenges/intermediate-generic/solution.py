"""
TODO:

The function `add` accepts two parameters of the same type and returns the same type.
"""

from typing import TypeVar

T = TypeVar('T')
def add(a, b: T) -> T:
    return a

def add[T](a:T, b: T) -> T:
    return a

## End of your code ##
from typing import List, assert_type

assert_type(add(1, 2), int)
assert_type(add("1", "2"), str)
assert_type(add(["1"], ["2"]), List[str])
