"""
TODO:

is_string is a function that returns a boolean result. If the result is True,
the argument passed in will be constrained to a certain type, namely type guard.
"""


def is_string(value):
    ...


def should_pass():
    a: str | None = "hello"
    if is_string(a):
        a.strip()


def should_fail():
    a: str | None = "hello"
    if not is_string(a):
        a.strip()
