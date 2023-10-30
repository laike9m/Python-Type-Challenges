"""
TODO:

Define a `Tree` type. `Tree` is a dictionary, whose keys are string, values are also `Tree`.
"""


def f(t: Tree):
    pass


def should_pass():
    f({})
    f({"foo": {}})
    f({"foo": {"bar": {}}})
    f({"foo": {"bar": {"baz": {}}}})


def should_fail():
    f(1)
    f({"foo": []})
    f({"foo": {1: {}}})
