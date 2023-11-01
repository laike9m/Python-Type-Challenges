"""
TODO:

foo is a function that when called with None value(default), returns an integer, otherwise it returns a string.
"""


def foo(value=None):
    ...


def should_pass():
    foo(42).upper()
    foo().bit_length()


def should_fail():
    foo(42).bit_length()
    foo().upper()
