"""
TODO:

is_string is a function that takes an argument value of arbitrary type, and returns a boolean.
You should make is_string be able to narrow the type of the argument based on its return value:
when it's true, narrow value's type to str.
Basically, it should work like `isinstance(value, str)` from the perspective of a type checker.
"""
from typing import Any


def is_string(value: Any):
    ...


def should_pass():
    a: str | None = "hello"
    if is_string(a):
        a.strip()


def should_fail():
    a: str | None = "hello"
    if not is_string(a):
        a.strip()
