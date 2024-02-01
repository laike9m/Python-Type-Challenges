"""
TODO:

Create a new type called Vector, which is a list of float.
"""

# Before 3.12 you have to write
# from typing import TypeAlias
#
# Vector: TypeAlias = list[float]

type Vector = list[float]


## End of your code ##
def foo(v: Vector):
    ...


foo([1.1, 2])
foo(1)  # expect-type-error
foo(["1"])  # expect-type-error
