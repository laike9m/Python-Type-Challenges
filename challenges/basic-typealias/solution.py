"""
TODO:

Create a new type called Vector, which is a list of float.
"""

from typing import TypeAlias

Vector: TypeAlias = list[float]

# Python >= 3.12
# type Vector = list[float]


## End of your code ##
def foo(v: Vector):
    ...


foo([1.1, 2])
foo(1)  # expect-type-error
foo(["1"])  # expect-type-error
