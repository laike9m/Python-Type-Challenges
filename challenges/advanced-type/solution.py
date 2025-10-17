"""
TODO:

`make_object` takes a class returns an instance of it.
"""


def make_object[T](cls: type[T]) -> T:
    ...


## End of your code ##
from typing import assert_type


class MyClass:
    pass


def f():
    pass


assert_type(make_object(MyClass), MyClass)
assert_type(make_object(int), int)

make_object(f)  # expect-type-error
make_object("sss")  # expect-type-error
make_object(["sss"])  # expect-type-error
