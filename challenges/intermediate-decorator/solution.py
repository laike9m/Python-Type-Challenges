"""
TODO:

Define a decorator that wraps a function and returns a function with the same signature.
"""
from typing import Callable, TypeVar

# For Python < 3.12
#
# T = TypeVar("T", bound=Callable)
#
# def decorator(func: T) -> T:
#     return func


# For Python >= 3.12
def decorator[T: Callable](func: T) -> T:
    return func


## End of your code ##
@decorator
def foo(a: int, *, b: str) -> None:
    ...


@decorator
def bar(c: int, d: str) -> None:
    ...


foo(1, b="2")
bar(c=1, d="2")

foo(1, "2")  # expect-type-error
foo(a=1, e="2")  # expect-type-error
decorator(1)  # expect-type-error
