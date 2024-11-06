"""
TODO:

foo should accept a empty tuple argument.
"""


def foo(x: tuple[()]):
    pass


## End of your code ##
foo(())
foo((1,))  # expect-type-error
