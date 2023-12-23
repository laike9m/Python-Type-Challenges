"""
TODO:

Define an `Array` type that supports element-wise addition of arrays with identical dimensions and types.
"""


class Array:
    def __add__(self, other):
        ...


## End of your code ##
from typing import assert_type

a: Array[float, int] = Array()
b: Array[float, int] = Array()
assert_type(a + b, Array[float, int])

c: Array[float, int, str] = Array()
assert_type(a + c, Array[float, int, str])  # expect-type-error
