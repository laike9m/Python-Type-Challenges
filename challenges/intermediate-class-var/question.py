"""
TODO:

Class `Foo` has a class variable `bar`, which is an integer.
"""

import typing


class Foo:
    """Hint: No need to write __init__"""


def should_pass():
    Foo.bar = 1


def should_fail():
    Foo.bar = "1"
