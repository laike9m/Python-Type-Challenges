"""
TODO:

foo should accept a dict argument, both keys and values are string.
"""


def foo(x):
    pass


def should_pass():
    foo({"foo": "bar"})


def should_fail():
    foo({"foo": 1})
