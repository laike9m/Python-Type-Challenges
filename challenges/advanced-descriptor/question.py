"""
TODO:

Create a descriptor and annotate the __get__ method.
"""


class Descriptor:
    def __get__(self, instance, owner):
        """you don't need to implement this"""
        ...


## End of your code ##
class TestClass:
    a = Descriptor()


def descriptor_self(x: Descriptor) -> None:
    ...


def string_value(x: str) -> None:
    ...


descriptor_self(TestClass.a)
string_value(TestClass().a)
descriptor_self(TestClass().a)  # expect-type-error
string_value(TestClass.a)  # expect-type-error
