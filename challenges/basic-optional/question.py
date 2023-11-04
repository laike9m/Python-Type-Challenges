"""
TODO:

foo can accept either an integer argument or no argument.
"""


def foo(x=0):
    pass


## End of your code ##
foo(10)
foo()

foo("10")  # expect-type-error
