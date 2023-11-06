"""
TODO:

foo only accepts literal 'left' and 'right' as its argument.
"""
from typing import Literal


def foo(direction: Literal["left", "right"]):
    ...


## End of your code ##
foo("left")
foo("right")

a = "left"
foo(a)  # expect-type-error
