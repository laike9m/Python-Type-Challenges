"""
TODO:

Define a wrapper type `Box` with generic parameter.
It is initialized with an object of the wrapped type and has a method to retrieve the wrapped value.
"""


class Box:
    def __init__(self, value):
        self.value = value

    def unwrap(self):
        # This should return the wrapped type
        return self.value


## End of your code ##
from typing import assert_type

assert_type(Box("1").unwrap(), str)
assert_type(Box(1).unwrap(), int)
assert_type(Box("1").unwrap(), int)  # expect-type-error
assert_type(Box(1).unwrap(), str)  # expect-type-error
