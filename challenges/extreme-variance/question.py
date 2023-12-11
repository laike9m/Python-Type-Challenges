"""
TODO: Annotate function `f` and `g`, to make tests pass.
"""


def f(a):
    pass


def g(a):
    pass


## End of your code ##

l1: list[int] = [1, 2]
f(l1)  # expect-type-error
g(l1)

l2: list[int | str] = [1, 2]
f(l2)
g(l2)

f(1)  # expect-type-error
f("1")  # expect-type-error
g(1)  # expect-type-error
g("1")
