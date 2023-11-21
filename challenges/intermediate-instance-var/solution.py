"""
TODO:

Class `Foo` has an instance variable `bar`, which is an integer.
"""


class Foo:
    bar: int


## End of your code ##
foo = Foo()
foo.bar = 1
foo.bar = "1"  # expect-type-error
