"""
TODO:

foo only accepts literal 'left' and 'right' as its argument.
"""


def foo(direction):
    ...


def should_pass():
    foo("left")
    foo("right")


def should_fail():
    a = "left"
    foo(a)
