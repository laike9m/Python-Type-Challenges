"""
TODO:

foo can accept an integer argument, None or no argument at all.
"""


def foo(x):
    pass


## End of your code ##
foo(10)
foo(None)
foo()

foo("10")  # expect-type-error
