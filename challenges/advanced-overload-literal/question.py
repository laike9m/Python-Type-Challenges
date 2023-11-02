"""
TODO:

foo is a function that returns an interger when second argument is 1, returns a string when second argument is 2, returns a list when second argument is 3, otherwise it returns inputs self.
"""


def foo(value, flag):
    ...


def should_pass():
    foo("42", 1).bit_length()
    foo(42, 2).upper()
    foo(True, 3).append(1)
    foo({}, "4").keys()


def should_fail():
    foo("42", 1).upper()
    foo(42, 2).append(1)
    foo(True, 3).bit_length()
    foo({}, "4").upper()
