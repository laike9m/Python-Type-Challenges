"""
TODO:

Define a `Array` type that supports addition of arrays with the same shape.
"""

from typing import Generic, TypeVar, TypeVarTuple

T = TypeVar("T")
Ts = TypeVarTuple("Ts")


class Array(Generic[*Ts]):
    def __add__(self, other: "Array[*Ts]") -> "Array[*Ts]":
        ...

    def add_dimension(self, x: "T") -> "Array[*Ts, T]":
        ...


## End of your code ##
a: Array[float, int] = Array()
b: Array[float, int] = Array()
print(a + b)

c: Array[float, int, str] = Array()
print(a + c)  # expect-type-error

d = a.add_dimension("foo")
print(c + d)
