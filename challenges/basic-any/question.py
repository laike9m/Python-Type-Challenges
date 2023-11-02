"""
TODO:

foo should accept an argument of arbitrary type.
"""


def foo(x):
    pass


## End of your code ##
foo(1)
foo("10")
foo(1, 2)  # expect-type-error
