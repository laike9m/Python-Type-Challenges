"""
TODO:

`Foo.return_self`'s return value should have the same type as the current enclosed class (i.e. `Foo`)
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
    sf: SubclassOfFoo = Foo().return_self()
