"""
TODO:

foo is a function that returns an interger when called with Foo[int], returns a string when called with Foo[str], otherwise returns a Foo[T].
"""
from typing import TypeVar, Generic

T = TypeVar("T")


class Foo(Generic[T]):
    a: T


def foo(value: Foo):
    ...


## End of your code ##

foo(Foo[int]()).bit_length()
foo(Foo[str]()).upper()
foo(Foo[list]()).a.append(1)

foo(Foo[int]()).upper()  # expect-type-error
foo(Foo[str]()).bit_length()  # expect-type-error
foo(Foo[list]()).bit_length()  # expect-type-error
