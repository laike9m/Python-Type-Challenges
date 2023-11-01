"""
TODO:
    Define a callable type that accepts a string parameter and returns None.
    *The parameter name can be any.*

HINT: Use Protocol
"""

from typing import Protocol


class SingleStringInput(Protocol):
    ...


def should_pass():
    def accept_single_string_input(func: SingleStringInput) -> None:
        ...

    def string_name(name: str) -> None:
        ...

    def string_value(value: str) -> None:
        ...

    accept_single_string_input(string_name)
    accept_single_string_input(string_value)


def should_fail():
    def accept_single_string_input(func: SingleStringInput) -> None:
        ...

    def int_value(value: int) -> None:
        ...

    def new_name(name: str) -> str:
        return name

    accept_single_string_input(int_value)
    accept_single_string_input(new_name)
