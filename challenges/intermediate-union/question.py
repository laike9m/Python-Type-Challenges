"""
TODO:

foo should accept a argument that's either a string or integer.
"""


def foo(x):
    pass


def should_pass():
    foo("foo")
    foo(1)


def should_fail():
    foo([])
