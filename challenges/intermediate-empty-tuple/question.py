"""
TODO:

foo should accept a empty tuple argument.
"""


def foo(x):
    pass


## End of your code ##
foo(())
foo((1,))  # expect-type-error
