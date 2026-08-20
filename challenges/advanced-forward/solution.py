# For Python < 3.14
#
# class MyClass:
#     def __init__(self, x: int) -> None:
#         self.x = x
#
#     # TODO: Fix the type hints of `copy` to make it type check
#     def copy(self) -> "MyClass":
#         copied_object = MyClass(x=self.x)
#         return copied_object
#
#
# Alternative solution:
#
# from __future__ import annotations
#
# class MyClass:
#     def __init__(self, x: int) -> None:
#         self.x = x
#
#     # TODO: Fix the type hints of `copy` to make it type check
#     def copy(self) -> MyClass:
#         copied_object = MyClass(x=self.x)
#         return copied_object


# For Python >= 3.14, Annotations are now lazily evaluated by default.
# See https://docs.python.org/3/reference/compound_stmts.html#annotations
class MyClass:
    def __init__(self, x: int) -> None:
        self.x = x

    # TODO: Fix the type hints of `copy` to make it type check
    def copy(self) -> MyClass:
        copied_object = MyClass(x=self.x)
        return copied_object


## End of your code ##

from typing import assert_type

inst = MyClass(x=1)
assert_type(inst.copy(), MyClass)
