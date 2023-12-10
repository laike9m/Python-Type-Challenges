"""
TODO:

Modify `foo` so it takes an argument of arbitrary type.
"""

from typing import Any


def foo(x: Any):
    """⬆️ Change me. No need to implement the function."""


## End of your code ##
foo(1)
foo("10")
foo(1, 2)  # expect-type-error
