from typing import Callable, Concatenate, Any, assert_type


class Fn[R, **P]():
    def __init__(self, f: Callable[P, R]) -> None:
        self.f = f

    def into_callable(self) -> Callable[Concatenate[Any, P], R]:
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
