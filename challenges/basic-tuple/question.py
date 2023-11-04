"""
TODO:

foo should accept a tuple argument, 1st item is a string, 2nd item is an integer.
"""


def foo(x):
    pass


## End of your code ##
foo(("foo", 1))

foo((1, 2))  # expect-type-error
foo(("foo", "bar"))  # expect-type-error
foo((1, "foo"))  # expect-type-error
