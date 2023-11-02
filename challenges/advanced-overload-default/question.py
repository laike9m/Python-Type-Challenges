"""
TODO:

foo is a function that returns an interger when second argument is True, otherwise it returns a string.
"""


def foo(value, flag=False):
    ...


def should_pass():
    foo("42").upper()
    foo("42", True).bit_length()


def should_fail():
    foo("42").bit_length()
    foo("42", True).upper()
