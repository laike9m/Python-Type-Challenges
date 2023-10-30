"""
TODO:

foo should accept a tuple argument, 1st item is a string, 2nd item is an integer.
"""


def foo(x):
    pass


def should_pass():
    foo(("foo", 1))


def should_fail():
    foo((1, 2))
    foo(("foo", "bar"))
    foo((1, "foo"))
