"""
TODO:

Define a function that accepts two parameters of the same type and returns the same type.
The type can only be str or int.
"""
from typing import TypeVar

T = TypeVar("T", int, str)

def add(a: T, b: T) -> T:
    return a

def add[T: (str,int)](a: T, b: T) -> T:
    return a

## End of your code ##
from typing import assert_type

assert_type(add(1, 2), int)
assert_type(add("1", "2"), str)

add(["1"], ["2"])  # expect-type-error
add("1", 2)  # expect-type-error
