"""
TODO:

Define a `Array` type that supports addition of arrays with the same shape.
"""

from typing import Generic, Tuple, TypeAlias, TypeVar, TypeVarTuple

T = TypeVar("T")
Ts = TypeVarTuple("Ts")

S1: TypeAlias = Tuple[float, int]
S2: TypeAlias = Tuple[*S1, str]


class Array(Generic[*Ts]):
    def __add__(self, other: "Array[*Ts]") -> "Array[*Ts]":
        ...

    def add_dimension(self, x: "T") -> "Array[*Ts, T]":
        ...


a: Array[*S1] = Array()
b: Array[*S1] = Array()
print(a + b)

c: Array[*S2] = Array()
print(a + c)  # expect-type-error
d = a.add_dimension("foo")
print(c + d)
