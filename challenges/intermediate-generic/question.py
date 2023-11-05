"""
TODO:

The function `add` accepts two parameters of the same type and returns the same type.
"""


def add(a, b):
    return a


## End of your code ##
from typing import List, assert_type

assert_type(add(1, 2), int)
assert_type(add("1", "2"), str)
assert_type(add(["1"], ["2"]), List[str])
