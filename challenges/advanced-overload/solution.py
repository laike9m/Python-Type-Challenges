"""
TODO:

foo is a function that when called with None value(default), returns an integer, otherwise it returns a string.
"""
from typing import Union, Optional, overload, Any

@overload
def foo()->int:
    ...

@overload
def foo(value: Any)->str:
    ...

def foo(value):
    ...


## End of your code ##
from typing import assert_type

assert_type(foo(42), str)
assert_type(foo(), int)

assert_type(foo(42), int)  # expect-type-error
assert_type(foo(), str)  # expect-type-error
