"""
TODO:

make Fn[VnCallable] could be casted to a Callable with a Any value.
you MUST NOT modify anything expect the `Fn.into_callable`'s annotation.
"""

from typing import Callable, TypeVar, Generic, Any, assert_type

VnCallable = TypeVar("VnCallable", bound=Callable)

class Fn(Generic[VnCallable]):
    def __init__(self, f: VnCallable) -> None:
        self.f = f

    def into_callable(self) -> None:
        ...


def should_pass():
    @Fn
    def example(a: int, b: str, c: float, *, d: bool = False) -> None:
        return

    assert_type(example.f(1, "1", 1., d=False), None)

    a: Any = 11111111

    b = example.into_callable()(a, 1, "1", 1., d=False)

    assert_type(b, None)


def should_fail():
    @Fn
    def example(a: int, b: str, c: float, *, d: bool = False) -> None:
        ...

    example.into_callable()(1, "1", 1., d=False)
