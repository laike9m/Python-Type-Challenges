"""
TODO:

Enhance the Fn[VnCallable].into_callable method to return a Callable with an additional
Any parameter at the beginning (using Concatenate).
This should preserve the remaining parts of the function signature from VnCallable
(i.e., parameters and their types, excluding the suffix), as well as the return type.
"""

from typing import Callable, Concatenate, ParamSpec, TypeVar, Generic, Any, assert_type

P = ParamSpec("P")
R = TypeVar("R", covariant=True)
VnCallable = TypeVar("VnCallable", bound=Callable)


class Fn(Generic[VnCallable]):
    def __init__(self, f: VnCallable) -> None:
        self.f = f

    def into_callable(self: "Fn[Callable[P, R]]") -> Callable[Concatenate[Any, P], R]:
        ...


## End of your code ##
@Fn
def example(a: int, b: str, c: float, *, d: bool = False) -> None:
    return


assert_type(example.f(1, "1", 1.0, d=False), None)

a: Any = 11111111
b = example.into_callable()(a, 1, "1", 1.0, d=False)
assert_type(b, None)

example.into_callable()(1, "1", 1.0, d=False)  # expect-type-error
