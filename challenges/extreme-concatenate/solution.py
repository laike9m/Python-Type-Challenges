"""
TODO:

Suppose there's a function `foo`, whose first parameter can be anything.

You want to use `foo`, but want to restrict the first argument to be a `Person`.
You cannot modify `foo`, so you decide to write a function `transform`,
to transform `foo` into the function you want.
"""

from typing import Concatenate, Callable, Any


class Person:
    pass


def transform[T, **P](f: Callable[Concatenate[Any, P], T]):
    def wrapper(value: Person, *args: P.args, **kwargs: P.kwargs) -> T:
        return f(value, *args, **kwargs)

    return wrapper


## End of your code ##
def foo(value, mode: str) -> None:
    pass


foo_with_person = transform(foo)
foo_with_person(Person(), "1")
foo_with_person(Person(), mode="1")
foo_with_person(1, "1")  # expect-type-error
foo_with_person(Person(), 1)  # expect-type-error
foo_with_person(Person(), "1", 2)  # expect-type-error


def foo2(value, mode: str, *, maybe: bool) -> int:
    return 1


foo_with_person = transform(foo2)
foo_with_person(Person(), "1", maybe=True)
foo_with_person(value=Person(), mode="1", maybe=True)
foo_with_person(Person(), mode="1", maybe=True)
foo_with_person(Person(), mode="1")  # expect-type-error
foo_with_person(Person(), 1, maybe=True)  # expect-type-error
foo_with_person(Person(), "1", maybe=1)  # expect-type-error
foo_with_person(Person(), "1", True)  # expect-type-error
