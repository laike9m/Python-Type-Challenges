"""
TODO:

a method-like descriptor, implements the `__get__` only.
"""
from typing import ParamSpec, TypeVar, Concatenate, Callable, Generic

P = ParamSpec("P")
T = TypeVar("T")
R = TypeVar("R")

class MyMethod(Generic[T, P, R]):
    def __init__(self, func: Callable[Concatenate[T, P], R]) -> None:
        self.func = func
    
    def __get__(self, instance, owner) -> None:
        return



def should_pass():
    class Foo:
        @MyMethod
        def do_something(self, value: int) -> None:
            ...

    foo = Foo()

    Foo.do_something(foo, 1111)
    foo.do_something(1111)


def should_fail():
    class Foo:
        @MyMethod
        def do_something(self, value: int) -> None:
            ...

    foo = Foo()

    Foo.do_something(1111)
    foo.do_something(11111, foo)
    foo.do_something(foo, 11111)
