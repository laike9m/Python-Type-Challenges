"""
TODO:

Define a descriptor, make test case works.
"""


class Descriptor:
    ...


def should_pass():
    class TestClass:
        a = Descriptor()
    
    def descriptor_self(x: Descriptor) -> None:
        ...

    def string_value(x: str) -> None:
        ...
    
    descriptor_self(TestClass.a)
    string_value(TestClass().a)


def should_fail():
    class TestClass:
        a = Descriptor()
    
    def descriptor_self(x: Descriptor) -> None:
        ...

    def string_value(x: str) -> None:
        ...
    
    descriptor_self(TestClass().a)
    string_value(TestClass.a)

