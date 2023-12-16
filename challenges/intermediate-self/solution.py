"""
TODO:

`return_self` should return an instance of the same type as the current enclosed class.
"""

from typing import Self


class Foo:
    def return_self(self) -> Self:
        ...


# Another solution using TypeVar
# from typing import TypeVar
#
# T = TypeVar('T', bound='Foo')
#
# class Foo:
#     def return_self(self: T) -> T:
#         ...


## End of your code ##
class SubclassOfFoo(Foo):
    pass


f: Foo = Foo().return_self()
sf: SubclassOfFoo = SubclassOfFoo().return_self()

sf: SubclassOfFoo = Foo().return_self()  # expect-type-error
