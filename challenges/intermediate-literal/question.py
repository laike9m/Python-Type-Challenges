"""
TODO:

foo only accepts literal 'left' and 'right' as its argument.
"""


def foo(direction):
    ...


## End of your code ##
foo("left")
foo("right")

a = "".join(["l", "e", "f", "t"])
foo(a)  # expect-type-error
