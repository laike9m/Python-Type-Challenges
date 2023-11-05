"""
TODO:

foo should accept a dict argument, both keys and values are string.
"""


def foo(x):
    pass


## End of your code ##
foo({"foo": "bar"})
foo({"foo": 1})  # expect-type-error
