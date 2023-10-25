"""
TODO:

foo should accept a argument that's either a string or integer.
"""


class Foo:
    def return_self(self):
        return self


class SubclassOfFoo(Foo):
    pass


# Test cases
def should_pass():
    f: Foo = Foo().return_self()
    sf: SubclassOfFoo = SubclassOfFoo().return_self()


def should_fail():
    sf: int = Foo().return_self()
