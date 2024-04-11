"""
TODO:

foo is a function that returns an integer when second argument is 1, returns a string when second argument is 2, returns a list when second argument is 3, otherwise it returns inputs self.
"""


def foo(value, flag):
    ...


## End of your code ##

foo("42", 1).bit_length()
foo(42, 2).upper()
foo(True, 3).append(1)
foo({}, "4").keys()

foo("42", 1).upper()  # expect-type-error
foo(42, 2).append(1)  # expect-type-error
foo(True, 3).bit_length()  # expect-type-error
foo({}, "4").upper()  # expect-type-error
