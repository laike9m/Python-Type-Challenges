"""
TODO:

Define an "tupled" function that accepts a function and returns a function with some arguments in the form of a tuple.
The return type should remain unchanged.
(if you're familiar with scala, this is effectively the "tupled" function)
"""
from typing import Callable


def tupled[*Ts, R](func: Callable[[*Ts], R]) -> Callable[[tuple[*Ts]], R]:
    def impl(args: tuple[*Ts]) -> R:
        return func(*args)

    return impl


## End of your code ##
from typing import Any


def func0() -> Any:
    ...


def func1(s: str) -> Any:
    ...


def func2(s: str, i: int) -> Any:
    ...


func0_tupled = tupled(func0)
func0_tupled(())
func0_tupled()  # expect-type-error

func1_tupled = tupled(func1)
func1_tupled(("a",))
func1_tupled("a")  # expect-type-error
func1_tupled(1)  # expect-type-error

func2_tupled = tupled(func2)
func2_tupled(("a", 1))
func2_tupled(("a", "b"))  # expect-type-error
func2_tupled("a", 1)  # expect-type-error
