"""
TODO:

Define an `Array` type that supports element-wise addition of arrays with identical dimensions and types.
"""

from typing import Generic, TypeVar, TypeVarTuple, assert_type

T = TypeVar("T")
Ts = TypeVarTuple("Ts")


class Array(Generic[*Ts]):
    def __add__(self, other: "Array[*Ts]") -> "Array[*Ts]":
        ...


## End of your code ##
from typing import assert_type

a: Array[float, int] = Array()
b: Array[float, int] = Array()
assert_type(a + b, Array[float, int])

c: Array[float, int, str] = Array()
assert_type(a + c, Array[float, int, str])  # expect-type-error
