"""
TODO:

foo should accept a list argument, whose elements are string.
"""


def foo(x):
    pass


# Test cases
def should_pass():
    foo(["foo", "bar"])


def should_fail():
    foo(["foo", 1])
