"""
TODO:

`is_string` determines whether the input value is a string.
Your job is to make the type checker be aware of this information.
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
    assert_type(a, type(None))  # expect-type-error
