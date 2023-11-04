"""
TODO:
    foo should accept a argument that's either a string or integer.
"""


def foo(x):
    pass


## End of your code ##
foo("foo")
foo(1)

foo([])  # expect-type-error
