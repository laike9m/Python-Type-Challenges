"""
TODO:

Define a generic class that represents a stack.
It can be instantiated with a certain type, with method `push` accepting an object of the specified type,
and `pop` returning an an object of the same type
"""


class Stack:
    def __init__(self) -> None:
        self.items = []

    def push(self, item) -> None:
        self.items.append(item)

    def pop(self):
        return self.items.pop()


## End of your code ##
from typing import assert_type

s = Stack[int]()
s.push(1)
assert_type(s.pop(), int)
s.push("foo")  # expect-type-error
assert_type(s.pop(), str)  # expect-type-error
