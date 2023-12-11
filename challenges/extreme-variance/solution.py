"""
Annotate function `f` and `g`, to make tests pass.
"""

from collections.abc import Sequence


def f(a: list[int | str]):
    pass


def g(a: Sequence[int | str]):
    pass


## End of your code ##

l1: list[int] = [1, 2]
f(l1)  # expect-type-error
g(l1)

l2: list[int | str] = [1, 2]
f(l2)
g(l2)
