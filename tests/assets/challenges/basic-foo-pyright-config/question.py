"""A simple question, only for running tests.
"""


def foo():
    pass


## End of your code ##
foo(1)
foo(1, 2)  # expect-type-error

## End of test code ##
# pyright: reportGeneralTypeIssues=error
