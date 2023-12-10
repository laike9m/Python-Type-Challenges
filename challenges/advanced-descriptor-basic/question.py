"""
TODO:

Create a descriptor and adorn the __get__ method with the @typing.overload decorator to ensure the functionality of the test case.

NOTE: Craft at least two overload declarations:

- one to handle the case when the instance is None (i.e., accessing TestClass.a), and another...
- ...to cater to any instance of TestClass.

NOTE: By explicitly binding the instance parameter to the TestClass class, the test cases can also be successfully passed.
"""


class Descriptor:
    def __get__(self, instance: ..., owner: ...):
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
