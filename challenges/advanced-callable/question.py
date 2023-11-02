"""
TODO:

Define a callable type that takes two arguments:

1. *arbitrary param name*: a string
2. `size`: an integer

Returns: None

HINT: Use Protocol
"""


class MyCallable:
    ...


def should_pass():
    def test_func(func: MyCallable) -> None:
        ...

    def name_size(name: str, size: int) -> None:
        ...

    def type_size(type_: str, size: int) -> None:
        ...

    test_func(name_size)
    test_func(type_size)


def should_fail():
    def test_func(func: MyCallable) -> None:
        ...

    def age_size(age: int, size: int) -> None:
        ...

    def name_age(name: str, age: int) -> None:
        ...

    def return_string(name: str, size: int) -> str:
        return name

    test_func(age_size)
    test_func(name_age)
    test_func(return_string)
