"""
TODO:

foo is a function that returns an interger when called with Foo[int], returns a string when called with Foo[str], otherwise returns a Foo[T].
"""
from typing import Any, TypeVar, Generic, overload

T = TypeVar('T')

class Foo(Generic[T]):
    a: T

@overload
def foo(value: Foo[int]) -> int:
    ...

@overload
def foo(value: Foo[str]) -> str:
    ...

@overload
def foo(value: Foo[T]) -> Foo[T]:
    ...

def foo(value: Foo) -> Any:
    ...


def should_pass():
    foo(Foo[int]()).bit_length()
    foo(Foo[str]()).upper()
    foo(Foo[list]()).a.append(1)


def should_fail():
    foo(Foo[int]()).upper()
    foo(Foo[str]()).bit_length()
    foo(Foo[list]()).bit_length()
