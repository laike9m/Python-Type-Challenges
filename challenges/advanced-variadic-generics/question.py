"""
TODO:

Define a `Array` type that supports addition of arrays with the same shape.
"""


class Array:
    def __add__(self, other):
        ...

    def add_dimension(self, x):
        ...


## End of your code ##
a: Array[float, int] = Array()
b: Array[float, int] = Array()
print(a + b)

c: Array[float, int, str] = Array()
print(a + c)  # expect-type-error

d = a.add_dimension("foo")
print(c + d)
