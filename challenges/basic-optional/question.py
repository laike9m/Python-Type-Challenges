"""
TODO:

foo can accept either an integer argument or no argument.
"""


def foo(x=0):
    pass


def should_pass():
    foo(10)
    foo()


def should_fail():
    foo("10")
