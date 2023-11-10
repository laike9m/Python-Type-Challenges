"""
TODO:

is_string is a function that takes an argument value of arbitrary type, and returns a boolean.
You should make is_string be able to narrow the type of the argument based on its return value:
when it's true, narrow value's type to str.
Basically, it should work like `isinstance(value, str)` from the perspective of a type checker.
"""
from typing import Any, TypeGuard


def is_string(value: Any) -> TypeGuard[str]:
    return isinstance(value, str)


## End of your code ##
from typing import assert_type

a: str | None = "hello"
if is_string(a):
    assert_type(a, str)
else:
    assert_type(a, type(None))
