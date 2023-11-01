"""
TODO:

Define a decorator that wraps a function and returns a function with the same signature.
"""


def decorator(func):
    ...


def should_pass():
    @decorator
    def foo(a: int, *, b: str) -> None:
        ...

    foo(1, b="2")


def should_fail():
    @decorator
    def foo(c: int, *, d: str) -> None:
        ...

    foo(1, "2")
    foo(c=1, e="2")
