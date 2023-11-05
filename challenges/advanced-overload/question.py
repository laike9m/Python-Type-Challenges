"""
TODO:

foo is a function that when called with None value(default), returns an integer, otherwise it returns a string.
"""


def foo(value=None):
    ...


## End of your code ##
from typing import assert_type

assert_type(foo(42), str)
assert_type(foo(), int)

assert_type(foo(42), int)  # expect-type-error
assert_type(foo(), str)  # expect-type-error
