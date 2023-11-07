"""
TODO:

Define a decorator that wraps a function and returns a function with the same signature.
"""
from typing import Callable, TypeVar, cast
from functools import wraps

T = TypeVar("T", bound=Callable)

def decorator(func: T) -> T:

    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return cast(T, wrapper)

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
