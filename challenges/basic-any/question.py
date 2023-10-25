"""
TODO:

foo should accept an argument of arbitrary type.
"""


def foo(x):
    pass


# Test cases
def should_pass():
    foo(1)
    foo("10")


def should_fail():
    foo(1, 2)
