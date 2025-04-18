"""
TODO:

Fn is a class decorator which takes a callable (`f`).
Fn has a `transform_callable` method, which transform `f` into a different callable,
with an additional Any parameter at the beginning, while preserving the remaining parts
of the function signature.

Note: you're only requried to add type annotations without implementing transform_callable.
"""


from typing import Callable, Concatenate, Generic, ParamSpec, TypeVar

# # For Python < 3.12
# R = TypeVar("R")
# P = ParamSpec("P")
#
#
# class Fn(Generic[R, P]):
#     def __init__(self, f: Callable[P, R]):
#         self.f = f
#
#     def transform_callable(self) -> Callable[Concatenate[object, P], R]:
#         ...


# For Python >= 3.12
class Fn[R, **P]:
    def __init__(self, f: Callable[P, R]) -> None:
        self.f = f

    def transform_callable(self) -> Callable[Concatenate[Any, P], R]:
        ...


## End of your code ##
from typing import assert_type, Any


@Fn
def example(a: int, b: str, c: float, *, d: bool = False) -> None:
    return


assert_type(example.f(1, "1", 1.0, d=False), None)

a: Any = 11111111
b = example.transform_callable()(a, 1, "1", 1.0, d=False)
assert_type(b, None)

example.transform_callable()(1, "1", 1.0, d=False)  # expect-type-error
