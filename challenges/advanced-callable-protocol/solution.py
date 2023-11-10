"""
TODO:

Define a callable type that accepts a string parameter called `name` and returns None.

HINT: Use Protocol
"""
from typing import Protocol


class SingleStringInput(Protocol):
    def __call__(self, name: str) -> None:
        ...

## End of your code ##
def accept_single_string_input(func: SingleStringInput) -> None:
    func(name="name")


def string_name(name: str) -> None:
    ...


def string_value(value: str) -> None:
    ...


def return_string(name: str) -> str:
    return name


accept_single_string_input(string_name)
accept_single_string_input(string_value)  # expect-type-error
accept_single_string_input(return_string)  # expect-type-error
