"""
TODO:

Define a callable type that accepts a string parameter called `name` and returns None.

HINT: Use Protocol
"""


class SingleStringInput:
    ...


def should_pass():
    def accept_single_string_input(func: SingleStringInput) -> None:
        func(name="name")

    def string_name(name: str) -> None:
        ...

    accept_single_string_input(string_name)


def should_fail():
    def accept_single_string_input(func: SingleStringInput) -> None:
        func(name="name")

    def string_value(value: str) -> None:
        ...

    def return_string(name: str) -> str:
        return name

    accept_single_string_input(string_value)
    accept_single_string_input(return_string)
