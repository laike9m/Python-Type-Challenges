"""
TODO:

Define a generic class that represents a stack.
It can be instantiated with a certain type, with method `push` accepting an object of the same type,
and `pop` returning an an object of the same type
"""
from typing import TypeVar, Generic, assert_type

# Before 3.12 you have to write:
# T = TypeVar('T')
# class Stack(Generic[T]):


# For Python >= 3.12
class Stack[T]():
    def __init__(self) -> None:
        self.items: list[T] = []  # This list[T] optional

    def push(self, item: T) -> None:
        self.items.append(item)

    # If `self.items: list[T]` is added above, annotation here can be ignored.
    def pop(self) -> T:
        return self.items.pop()


## End of your code ##
from typing import assert_type

s = Stack[int]()
s.push(1)
assert_type(s.pop(), int)
s.push("foo")  # expect-type-error
assert_type(s.pop(), str)  # expect-type-error
