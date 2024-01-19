"""
TODO:

Please add type hints to the function `abort` to make the test pass.
"""


def abort():
    raise RuntimeError("abort")


## End of your code ##
from typing import assert_type


def main(arg: int | None) -> None:
    if arg is None:
        abort()

    print(arg + 42)
    assert_type(arg, int)
