"""
TODO:

Define a decorator `constructor_parameter` that accepts the type of Foo.
and return a wrapper function with the same signature as the constructor of Foo, 
and function decorated by `constructor_parameter` can be called with an instance of Foo.
"""
from typing import TypeVar, Callable
from typing_extensions import ParamSpec, Concatenate

class Foo:
    a: int
    b: str

    def __init__(self, a: int, b: str) -> None:
        ...

T = TypeVar('T')
P = ParamSpec('P')
R = TypeVar('R')


def constructor_parameter(cls: Callable[P, T]) -> Callable[[Callable[[T], R]], Callable[P, R]]:
    ...


def should_pass():
    @constructor_parameter(Foo)
    def func(foo: Foo) -> list[Foo]:
        ...

    res = func(1, "2")
    res[0].a.bit_length()
    res[0].b.upper()


def should_fail():
    @constructor_parameter(Foo)
    def func(foo: Foo) -> list:
        ...

    func("1", "2")
    func([1, 2, 3])
