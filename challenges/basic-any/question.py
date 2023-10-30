"""
TODO:

foo should accept an argument of arbitrary type.
"""

import typing


def foo(x):
    pass


def should_pass():
    foo(1)
    foo("10")


def should_fail():
    foo(1, 2)
