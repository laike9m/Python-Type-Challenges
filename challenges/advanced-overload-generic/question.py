"""
TODO:

foo is a function that returns an interger when called with Foo[int], returns a string when called with Foo[str], otherwise returns a Foo[T].
"""
from typing import TypeVar, Generic

T = TypeVar('T')

class Foo(Generic[T]):
    a: T

def foo(value: Foo):
    ...


def should_pass():
    foo(Foo[int]()).bit_length()
    foo(Foo[str]()).upper()
    foo(Foo[list]()).a.append(1)


def should_fail():
    foo(Foo[int]()).upper()
    foo(Foo[str]()).bit_length()
    foo(Foo[list]()).bit_length()
