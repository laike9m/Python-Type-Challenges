"""
TODO:

Class `Foo` has an instance variable `bar`, which is an integer.
"""


class Foo:
    """Hint: No need to write __init__"""


def should_pass():
    foo = Foo()
    foo.bar = 1


def should_fail():
    foo = Foo()
    foo.bar = "1"
