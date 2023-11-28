"""
TODO:

Add type annotations to the class `Wrap`, so that it can be called with the
same arguments as the function it wraps.
"""
from typing import Callable

# Before 3.12 you have to write:
# T = TypeVar('T')
# P = ParamSpec('P')
# class Wrap(Generic[T, P]):


# For Python >= 3.12
class Wrap[T, **P]:
    def __init__(self, func: Callable[P, T]) -> None:
        self.func = func

    def __call__(self, *args: P.args, **kwargs: P.kwargs) -> T:
        return self.func(*args, **kwargs)


## End of your code ##
from typing import assert_type


@Wrap
def add(a: int, b: int) -> int:
    return a + b


@Wrap
def replace_wildcard(string: str, replacement: str, *, count: int = -1) -> str:
    return string.replace("*", replacement, count)


assert_type(add(1, 2), int)
assert_type(replace_wildcard("Hello *", "World"), str)
assert_type(replace_wildcard("Hello *", "World", count=1), str)
replace_wildcard("Hello *", 1)  # expect-type-error
replace_wildcard("Hello *", "World", 1)  # expect-type-error
